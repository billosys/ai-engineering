;; Deterministic Markdown-frontmatter inventory for Project08 Slice01.
;; Fennel owns discovery, missing/unterminated handling, hashing, ordering, and
;; JSON report assembly. YAML::XS 0.82 is invoked only as the established parser
;; bridge; JSON::PP 4.06 emits canonical parsed value/shape fragments.

(local io io)
(local string string)
(local table table)

(fn shell-quote [value]
  (.. "'" (string.gsub value "'" "'\\''") "'"))

(fn run [command]
  (let [pipe (assert (io.popen command "r"))
        output (pipe:read "*a")]
    (let [(ok why code) (pipe:close)]
    (when (not ok) (error (.. "command failed (" (or why "unknown") ":" (or code "?") "): " command)))
      output)))

(fn json-string [value]
  (let [replacements {"\\" "\\\\" "\"" "\\\"" "\n" "\\n" "\r" "\\r" "\t" "\\t"}]
    (.. "\"" (string.gsub value "[\\\"\n\r\t]" (fn [char] (or (. replacements char) char))) "\"")))

(fn parser-records [manifest]
  ;; YAML::XS 0.82 is the parser bridge. Fennel supplies the deterministic,
  ;; hash-bearing manifest and assembles the final report; Perl only turns each
  ;; YAML block into a canonical JSON parser result.
  (let [program "use strict; use warnings; use Digest::SHA qw(sha256_hex); use YAML::XS qw(Load); use JSON::PP; binmode STDOUT, q{:encoding(UTF-8)}; my $m=shift; open my $in, q{<:raw}, $m or die $!; my $j=JSON::PP->new->canonical; sub shape { my ($x)=@_; return q{null} if !defined $x; return {mapping=>{map { $_=>shape($x->{$_}) } sort keys %$x}} if ref($x) eq q{HASH}; return {sequence=>[sort map { $j->encode(shape($_)) } @$x]} if ref($x) eq q{ARRAY}; return q{scalar} } while (<$in>) { chomp; my $p=$_; my $r={path=>$p}; open my $fh, q{<:raw}, $p or do { $r->{sha256}=undef; $r->{frontmatter}=JSON::PP::false; $r->{error}=q{unreadable-input}; print $j->encode($r), qq{\\n}; next }; local $/; my $t=<$fh>; $r->{sha256}=sha256_hex($t); if ($t !~ /\\A---\\r?\\n/) { $r->{frontmatter}=JSON::PP::false; $r->{error}=q{no-opening-frontmatter}; print $j->encode($r), qq{\\n}; next } if ($t !~ /\\A---\\r?\\n(.*?)^---\\s*$/ms) { $r->{frontmatter}=JSON::PP::false; $r->{error}=q{unterminated-frontmatter}; print $j->encode($r), qq{\\n}; next } my $v=eval { Load($1) }; if ($@) { $r->{frontmatter}=JSON::PP::false; $r->{error}=q{YAML::XS: }. $@; print $j->encode($r), qq{\\n}; next } if (ref($v) ne q{HASH}) { $r->{frontmatter}=JSON::PP::false; $r->{error}=q{non-mapping-frontmatter}; print $j->encode($r), qq{\\n}; next } $r->{frontmatter}=JSON::PP::true; $r->{keys}=[sort keys %$v]; $r->{shapes}={map { $_=>shape($v->{$_}) } sort keys %$v}; $r->{values}=$v; print $j->encode($r), qq{\\n} }"
        output (run (.. "perl -MYAML::XS -MJSON::PP -e " (shell-quote program) " -- " (shell-quote manifest)))]
    (let [records []]
      (string.gsub output "[^\n]+" (fn [line] (table.insert records line)))
      records)))

(fn closing-frontmatter [text]
  (if (not (string.match text "^%-%-%-%\r?\n")) nil
      (string.find text "\n%-%-%-%s*\n" 4)))

(fn files-under [root]
  (let [ok (os.execute (.. "test -d " (shell-quote root)))]
  (if (not (or (= ok true) (= ok 0)))
      nil
      (let [raw (run (.. "LC_ALL=C find " (shell-quote root) " -type f -name '*.md' -print0 | LC_ALL=C sort -z"))]
        (let [paths []]
          (string.gsub raw "[^\0]+" (fn [path] (table.insert paths path)))
          paths)))))

(fn main [args]
  (when (< (# args) 2)
    (error "usage: fennel inventory-frontmatter.fnl OUTPUT.json ROOT..."))
  (let [output-path (. args 1)
        roots []
        records []
        manifest (os.tmpname)]
    (for [index 2 (# args)] (table.insert roots (. args index)))
    (let [manifest-file (assert (io.open manifest "wb"))]
      (each [_ root (ipairs roots)]
        (let [paths (files-under root)]
          (if paths
              (each [_ path (ipairs paths)] (manifest-file:write path "\n"))
              (table.insert records (.. "{\"path\":" (json-string root) ",\"sha256\":null,\"frontmatter\":false,\"error\":\"missing-root\"}")))))
      (manifest-file:close))
    (each [_ record (ipairs (parser-records manifest))] (table.insert records record))
    (os.remove manifest)
    (let [root-json []]
      (each [_ root (ipairs roots)] (table.insert root-json (json-string root)))
      (let [file (assert (io.open output-path "wb"))]
        (file:write (.. "{\"roots\":[" (table.concat root-json ",") "],\"records\":[" (table.concat records ",") "]}\n"))
      (file:close)))))

(main arg)
