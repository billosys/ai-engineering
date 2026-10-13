#!/usr/bin/env ruby
# Normalize only the four exact historical list sentinels in design concept-card frontmatter.
require 'digest'
require 'json'
require 'English'
require 'pathname'
require 'tempfile'
require 'psych'

module DesignCardMetadata
  ALLOWED_LISTS = %w[aliases prerequisites extends contrasts_with].freeze
  STANDARD_TAG_PREFIX = 'tag:yaml.org,2002:'.freeze
  ROOT = File.realpath(File.expand_path('..', __dir__))

  def self.fail!(message)
    raise ArgumentError, message
  end

  def self.reject_unsafe_ast!(node, path, seen = {})
    case node
    when Psych::Nodes::Alias
      fail!("#{path}: YAML aliases are not supported")
    when Psych::Nodes::Scalar
      if node.anchor
        fail!("#{path}: YAML anchors are not supported")
      end
      if node.tag && !node.tag.start_with?(STANDARD_TAG_PREFIX)
        fail!("#{path}: custom YAML tag is not supported")
      end
    when Psych::Nodes::Sequence
      fail!("#{path}: YAML anchors are not supported") if node.anchor
      fail!("#{path}: custom YAML tag is not supported") if node.tag && !node.tag.start_with?(STANDARD_TAG_PREFIX)
      node.children.each { |child| reject_unsafe_ast!(child, path, seen) }
    when Psych::Nodes::Mapping
      fail!("#{path}: YAML anchors are not supported") if node.anchor
      fail!("#{path}: custom YAML tag is not supported") if node.tag && !node.tag.start_with?(STANDARD_TAG_PREFIX)
      keys = {}
      node.children.each_slice(2) do |key, value|
        fail!("#{path}: mapping key must be a scalar") unless key.is_a?(Psych::Nodes::Scalar)
        fail!("#{path}: YAML merge keys are not supported") if key.value == '<<'
        identity = key.value
        fail!("#{path}: duplicate YAML key #{identity.inspect}") if keys.key?(identity)
        keys[identity] = true
        reject_unsafe_ast!(key, path, seen)
        reject_unsafe_ast!(value, path, seen)
      end
    else
      fail!("#{path}: unsupported YAML node #{node.class}")
    end
  end

  def self.split_frontmatter(bytes, path)
    utf8 = bytes.dup.force_encoding(Encoding::UTF_8)
    fail!("#{path}: invalid UTF-8") unless utf8.valid_encoding?
    data = bytes.dup.force_encoding(Encoding::BINARY)
    fail!("#{path}: UTF-8 BOM is not supported") if data.byteslice(0, 3) == "\xEF\xBB\xBF".b
    fail!("#{path}: expected leading --- LF delimiter") unless data.start_with?("---\n")
    match = /^---\r?$/n.match(data, 4)
    fail!("#{path}: closing frontmatter delimiter not found") unless match
    close_start = match.begin(0)
    yaml = data.byteslice(4, close_start - 4)
    body = data.byteslice(match.end(0), data.bytesize - match.end(0)) || ''.b
    [yaml, body]
  end

  def self.load_metadata(yaml, path)
    stream = Psych.parse_stream(yaml)
    fail!("#{path}: expected exactly one YAML document") unless stream.children.length == 1
    document = stream.children.first
    root = document.root
    fail!("#{path}: frontmatter root must be a mapping") unless root.is_a?(Psych::Nodes::Mapping)
    reject_unsafe_ast!(root, path)
    value = Psych.safe_load(yaml, permitted_classes: [], permitted_symbols: [], aliases: false)
    fail!("#{path}: frontmatter root must load as a mapping") unless value.is_a?(Hash)
    fail!("#{path}: root metadata keys must be strings") unless value.keys.all? { |key| key.is_a?(String) }
    value.each do |key, item|
      if item.is_a?(Array) && item == [[]] && ALLOWED_LISTS.include?(key)
        next
      end
      validate_value!(item, path, key)
    end
    value
  rescue Psych::Exception => error
    fail!("#{path}: YAML parse/load error: #{error.class}: #{error.message.lines.first.to_s.strip}")
  end

  def self.validate_value!(value, path, at)
    case value
    when String, NilClass, TrueClass, FalseClass, Integer, Float
      true
    when Array
      value.each_with_index { |child, index| validate_value!(child, path, "#{at}[#{index}]") }
    when Hash
      value.each do |key, child|
        fail!("#{path}: non-string mapping key at #{at}") unless key.is_a?(String)
        validate_value!(child, path, "#{at}.#{key}")
      end
    else
      fail!("#{path}: unsupported value type #{value.class} at #{at}")
    end
  end

  def self.quote_string(value)
    JSON.generate(value, ascii_only: false)
  end

  def self.render_key(key)
    key.match?(/\A[A-Za-z0-9_-]+\z/) ? key : quote_string(key)
  end

  def self.scalar?(value)
    !(value.is_a?(Array) || value.is_a?(Hash))
  end

  def self.render_scalar(value)
    case value
    when String then quote_string(value)
    when NilClass then 'null'
    when TrueClass then 'true'
    when FalseClass then 'false'
    when Integer, Float then JSON.generate(value, ascii_only: false)
    else fail!("unsupported scalar type #{value.class}")
    end
  end

  def self.render_block(value, depth)
    spaces = ' ' * depth
    case value
    when Hash
      return [spaces + '{}'] if value.empty?
      lines = []
      value.each do |key, child|
        fail!('non-string mapping key during emission') unless key.is_a?(String)
        prefix = spaces + render_key(key) + ':'
        if scalar?(child)
          lines << prefix + ' ' + render_scalar(child)
        elsif child.empty?
          lines << prefix + (child.is_a?(Array) ? ' []' : ' {}')
        else
          lines << prefix
          lines.concat(render_block(child, depth + 2))
        end
      end
      lines
    when Array
      return [spaces + '[]'] if value.empty?
      lines = []
      value.each do |child|
        if scalar?(child)
          lines << spaces + '- ' + render_scalar(child)
        elsif child.empty?
          lines << spaces + '- ' + (child.is_a?(Array) ? '[]' : '{}')
        else
          lines << spaces + '-'
          lines.concat(render_block(child, depth + 2))
        end
      end
      lines
    else
      [spaces + render_scalar(value)]
    end
  end

  def self.transform(metadata)
    result = metadata.dup
    ALLOWED_LISTS.each do |key|
      result[key] = [] if result.key?(key) && result[key] == [[]]
    end
    result
  end

  def self.process(path)
    absolute = File.expand_path(path)
    fail!("#{path}: path is outside the repository") unless absolute.start_with?(ROOT + File::SEPARATOR)
    relative = Pathname.new(absolute).relative_path_from(Pathname.new(ROOT)).to_s
    fail!("#{path}: only tracked .md concept cards under knowledge/design/concept-cards are allowed") unless relative.match?(%r{\Aknowledge/design/concept-cards/.+\.md\z})
    current = ROOT
    relative.split(File::SEPARATOR).each do |part|
      current = File.join(current, part)
      fail!("#{path}: symlinks are not supported") if File.symlink?(current)
    end
    fail!("#{path}: not a regular file") unless File.file?(absolute)
    tracked = IO.popen(['git', '-C', ROOT, 'ls-files', '--error-unmatch', '--', relative], 'r', &:read)
    status = $CHILD_STATUS
    fail!("#{path}: not tracked by git") unless status&.success? && tracked.lines.map(&:strip) == [relative]

    original = File.binread(absolute)
    yaml, body = split_frontmatter(original, relative)
    metadata = load_metadata(yaml, relative)
    transformed = transform(metadata)
    rendered = render_block(transformed, 0).join("\n")
    output = ("---\n" + rendered + "\n---").b + body
    output.force_encoding(Encoding::UTF_8)
    fail!("#{path}: proposed output is invalid UTF-8") unless output.valid_encoding?
    # Reparse the proposed bytes before any caller can write them.
    candidate_yaml, candidate_body = split_frontmatter(output, relative)
    candidate = load_metadata(candidate_yaml, relative)
    fail!("#{path}: emitter failed typed round trip") unless candidate == transformed && candidate_body == body
    {
      'path' => relative,
      'input_sha256' => Digest::SHA256.hexdigest(original),
      'output_sha256' => Digest::SHA256.hexdigest(output),
      'metadata' => metadata,
      'transformed_metadata' => transformed,
      'body_bytes' => body.bytesize,
      'body_sha256' => Digest::SHA256.hexdigest(body),
      'output' => output,
      '_original_bytes' => original
    }
  end

  def self.target_path!(record)
    relative = record.fetch('path')
    fail!("#{relative}: path is outside the allowed concept-card tree") unless relative.match?(%r{\Aknowledge/design/concept-cards/.+\.md\z})
    absolute = File.expand_path(relative, ROOT)
    fail!("#{relative}: path is outside the repository") unless absolute.start_with?(ROOT + File::SEPARATOR)
    current = ROOT
    relative.split(File::SEPARATOR).each do |part|
      current = File.join(current, part)
      fail!("#{relative}: symlink target is not allowed") if File.symlink?(current)
    end
    fail!("#{relative}: target is not a regular file") unless File.file?(absolute)
    tracked = IO.popen(['git', '-C', ROOT, 'ls-files', '--error-unmatch', '--', relative], 'r', &:read)
    status = $CHILD_STATUS
    fail!("#{relative}: target is no longer tracked") unless status&.success? && tracked.lines.map(&:strip) == [relative]
    absolute
  end

  def self.ensure_unchanged!(record)
    path = target_path!(record)
    observed = Digest::SHA256.hexdigest(File.binread(path))
    expected = record.fetch('input_sha256')
    fail!("#{record['path']}: input changed after prevalidation (expected #{expected}, found #{observed})") unless observed == expected
    path
  end

  def self.atomic_replace(path, bytes, &before_replace)
    stat = File.stat(path)
    temp = Tempfile.new(['.normalize-design-card-', '.tmp'], File.dirname(path), binmode: true)
    begin
      temp.write(bytes)
      temp.flush
      temp.fsync
      temp.chmod(stat.mode & 0o777)
      temp.close
      return false if before_replace && !before_replace.call
      File.rename(temp.path, path)
    ensure
      temp.close! rescue nil
    end
  end

  def self.recover_written!(record, restored, held, recovery_failed)
    relative = record.fetch('path')
    begin
      absolute = File.expand_path(relative, ROOT)
      unless absolute.start_with?(ROOT + File::SEPARATOR) && relative.match?(%r{\Aknowledge/design/concept-cards/.+\.md\z})
        recovery_failed << "#{relative} (path is outside the allowed concept-card tree)"
        return
      end
      current = ROOT
      relative.split(File::SEPARATOR).each do |part|
        current = File.join(current, part)
        if File.symlink?(current)
          held << "#{relative} (target or parent is now a symlink)"
          return
        end
      end
      unless File.file?(absolute)
        held << "#{relative} (target is missing or not a regular file)"
        return
      end
      tracked = IO.popen(['git', '-C', ROOT, 'ls-files', '--error-unmatch', '--', relative], 'r', &:read)
      status = $CHILD_STATUS
      unless status&.success? && tracked.lines.map(&:strip) == [relative]
        recovery_failed << "#{relative} (target is no longer tracked)"
        return
      end
      current_bytes = File.binread(absolute)
      unless current_bytes == record.fetch('output').b
        held << "#{relative} (current bytes differ from this command's output)"
        return
      end
      hold_reason = nil
      replaced = atomic_replace(absolute, record.fetch('_original_bytes')) do
        current_path = ROOT
        relative.split(File::SEPARATOR).each do |part|
          current_path = File.join(current_path, part)
          if File.symlink?(current_path)
            hold_reason = 'target or parent became a symlink before recovery replacement'
            break
          end
        end
        if hold_reason
          false
        elsif !File.file?(absolute)
          hold_reason = 'target became missing or non-regular before recovery replacement'
          false
        elsif File.binread(absolute) != record.fetch('output').b
          hold_reason = 'current bytes changed before recovery replacement'
          false
        else
          true
        end
      end
      if replaced
        restored << relative
      else
        held << "#{relative} (#{hold_reason || 'recovery replacement was not performed'})"
      end
    rescue StandardError => error
      recovery_failed << "#{relative} (#{error.class}: #{error.message})"
    end
  end

  def self.hold_unwritten_drift!(record, held)
    relative = record.fetch('path')
    absolute = File.expand_path(relative, ROOT)
    unless absolute.start_with?(ROOT + File::SEPARATOR) && relative.match?(%r{\Aknowledge/design/concept-cards/.+\.md\z})
      held << "#{relative} (path is outside the allowed concept-card tree)"
      return
    end
    current = ROOT
    relative.split(File::SEPARATOR).each do |part|
      current = File.join(current, part)
      if File.symlink?(current)
        held << "#{relative} (target or parent is now a symlink)"
        return
      end
    end
    unless File.file?(absolute)
      held << "#{relative} (target is missing or not a regular file)"
      return
    end
    observed = Digest::SHA256.hexdigest(File.binread(absolute))
    expected = record.fetch('input_sha256')
    held << "#{relative} (current bytes differ from prevalidated input #{expected}; found #{observed})" unless observed == expected
  rescue StandardError => error
    held << "#{relative} (unable to inspect after interruption: #{error.class}: #{error.message})"
  end

  def self.report_interruption!(written, restored, held, recovery_failed, original_error)
    warn "normalize-design-card-metadata: batch interrupted by #{original_error.class}: #{original_error.message}"
    warn "normalize-design-card-metadata: written: #{written.empty? ? 'none' : written.map { |r| r['path'] }.join(', ')}"
    warn "normalize-design-card-metadata: restored: #{restored.empty? ? 'none' : restored.join(', ')}"
    warn "normalize-design-card-metadata: held: #{held.empty? ? 'none' : held.join('; ')}"
    warn "normalize-design-card-metadata: recovery-failed: #{recovery_failed.empty? ? 'none' : recovery_failed.join('; ')}"
  end

  def self.write_records!(records)
    written = []
    begin
      records.each { |record| ensure_unchanged!(record) }
      records.each do |record|
        target = ensure_unchanged!(record)
        replaced = atomic_replace(target, record.fetch('output')) do
          ensure_unchanged!(record)
          true
        end
        fail!("#{record['path']}: replacement was not performed") unless replaced
        written << record
      end
    rescue StandardError => original_error
      restored = []
      held = []
      recovery_failed = []
      written.reverse_each do |record|
        recover_written!(record, restored, held, recovery_failed)
      end
      records.each do |record|
        hold_unwritten_drift!(record, held) unless written.include?(record) || held.any? { |item| item.start_with?(record['path'] + ' ') }
      end
      report_interruption!(written, restored, held, recovery_failed, original_error)
      records.each { |record| record['_original_bytes'].clear }
      raise original_error
    end
  end
end

if $PROGRAM_NAME == __FILE__
  begin
    mode = ARGV.shift
    if ARGV.empty?
      warn 'usage: ruby scripts/normalize-design-card-metadata.rb --check|--write PATH...'
      exit 2 if mode
      exit 0
    end
    unless %w[--check --write].include?(mode)
      warn 'first argument must be --check or --write'
      exit 2
    end
    paths = ARGV.dup
    expanded = paths.map { |path| File.expand_path(path) }
    raise ArgumentError, 'repeated input path' unless expanded.uniq.length == expanded.length
    records = paths.map { |path| DesignCardMetadata.process(path) }
    DesignCardMetadata.write_records!(records) if mode == '--write'
    records.each do |record|
      record['_original_bytes'].clear
      record.delete('_original_bytes')
      record.delete('output')
      puts JSON.generate(record, ascii_only: false)
    end
  rescue StandardError => error
    warn "normalize-design-card-metadata: #{error.message}"
    exit 1
  end
end
