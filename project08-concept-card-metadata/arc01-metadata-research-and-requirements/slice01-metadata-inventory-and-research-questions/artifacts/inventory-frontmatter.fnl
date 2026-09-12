;; Deterministic Markdown-frontmatter inventory for Project08 Slice01.
;; Fennel owns discovery, framing, hashing, typed-shape/path traversal, and
;; report/index assembly. YAML::XS parses already-framed YAML blocks only.
;; YAML::XS is configured with JSON::PP booleans, preserving true/false rather
;; than colliding with 1/"". It uses YAML 1.1-style implicit typing; timestamps
;; are emitted as strings and explicit YAML tags are not retained.

(local io io)
(local os os)
(local string string)
(local table table)
(local array-marker {})
(local null-marker {})

(fn shell-quote [value] (.. "'" (string.gsub value "'" "'\\''") "'"))

(fn run [command]
  (let [pipe (assert (io.popen command "r")) output (pipe:read "*a") (ok why code) (pipe:close)]
    (when (not ok) (error (.. "command failed (" (or why "unknown") ":" (or code "?") "): " command)))
    output))

(fn sorted-keys [value]
  (let [keys []]
    (rawset keys array-marker true)
    (each [key _ (pairs value)] (when (= (type key) "string") (table.insert keys key)))
    (table.sort keys) keys))

(fn array? [value] (and (= (type value) "table") (= (rawget value array-marker) true)))

(fn json-string [value]
  (let [replacements {"\\" "\\\\" "\"" "\\\"" "\n" "\\n" "\r" "\\r" "\t" "\\t"}]
    (.. "\"" (string.gsub value "[\\\"\n\r\t]" (fn [char] (or (. replacements char) char))) "\"")))

(fn json-encode [value]
  (if (= value null-marker) "null"
      (= value true) "true"
      (= value false) "false"
      (= (type value) "string") (json-string value)
      (= (type value) "number") (tostring value)
      (array? value) (let [parts []]
                       (for [index 1 (# value)] (table.insert parts (json-encode (. value index))))
                       (.. "[" (table.concat parts ",") "]"))
      (= (type value) "table") (let [parts []]
                                (each [_ key (ipairs (sorted-keys value))]
                                  (table.insert parts (.. (json-string key) ":" (json-encode (. value key)))))
                                (.. "{" (table.concat parts ",") "}"))
      (error (.. "cannot encode JSON value of type " (type value)))))

;; Parser output is data, not an executable helper. This accepts JSON::PP JSON.
(fn json-decode [text]
  (var position 1)
  (fn byte [] (string.sub text position position))
  (fn skip-space [] (while (string.match (byte) "%s") (set position (+ position 1))))
  (fn expect [token]
    (when (not (= (string.sub text position (+ position (# token) -1)) token))
      (error (.. "invalid JSON at byte " position "; expected " token)))
    (set position (+ position (# token))))
  (fn utf8 [code]
    (if (< code 128) (string.char code)
        (< code 2048) (string.char (+ 192 (math.floor (/ code 64))) (+ 128 (% code 64)))
        (string.char (+ 224 (math.floor (/ code 4096))) (+ 128 (% (math.floor (/ code 64)) 64)) (+ 128 (% code 64)))))
  (var parse-value nil)
  (fn parse-string []
    (expect "\"")
    (let [parts []]
      (while (not (= (byte) "\""))
        (when (= (byte) "") (error "unterminated JSON string"))
        (if (= (byte) "\\")
            (do
              (set position (+ position 1))
              (let [escape (byte)]
                (if (= escape "\"") (table.insert parts "\"")
                    (= escape "\\") (table.insert parts "\\")
                    (= escape "/") (table.insert parts "/")
                    (= escape "b") (table.insert parts "\b")
                    (= escape "f") (table.insert parts "\f")
                    (= escape "n") (table.insert parts "\n")
                    (= escape "r") (table.insert parts "\r")
                    (= escape "t") (table.insert parts "\t")
                    (= escape "u") (let [hex (string.sub text (+ position 1) (+ position 4)) code (tonumber hex 16)]
                                        (when (not code) (error "invalid JSON unicode escape"))
                                        (table.insert parts (utf8 code))
                                        (set position (+ position 4)))
                    (error (.. "invalid JSON escape " escape))))
              (set position (+ position 1)))
            (do (table.insert parts (byte)) (set position (+ position 1)))))
      (set position (+ position 1))
      (table.concat parts)))
  (fn parse-array []
    (expect "[")
    (let [result {}]
      (rawset result array-marker true) (skip-space)
      (if (= (byte) "]")
          (set position (+ position 1))
          (do (table.insert result (parse-value)) (skip-space)
              (while (= (byte) ",") (set position (+ position 1)) (skip-space) (table.insert result (parse-value)) (skip-space))
              (expect "]")))
      result))
  (fn parse-object []
    (expect "{")
    (var more true)
    (let [result {}]
      (skip-space)
      (if (= (byte) "}")
          (set position (+ position 1))
          (while more
              (let [key (parse-string)]
                (skip-space) (expect ":") (skip-space) (tset result key (parse-value)) (skip-space)
                (if (= (byte) ",") (do (set position (+ position 1)) (skip-space))
                    (do (expect "}") (set more false))))))
      result))
  (set parse-value
    (fn []
      (skip-space)
      (let [current (byte)]
        (if (= current "\"") (parse-string)
            (= current "{") (parse-object)
            (= current "[") (parse-array)
            (= (string.sub text position (+ position 3)) "true") (do (expect "true") true)
            (= (string.sub text position (+ position 4)) "false") (do (expect "false") false)
            (= (string.sub text position (+ position 3)) "null") (do (expect "null") null-marker)
            (let [number-text (string.match (string.sub text position) "^-?%d+%.?%d*[eE]?[+-]?%d*")]
              (when (not number-text) (error (.. "invalid JSON value at byte " position)))
              (set position (+ position (# number-text))) (tonumber number-text))))))
  (let [result (parse-value)]
    (skip-space) (when (<= position (# text)) (error (.. "trailing JSON at byte " position))) result))

(fn shape-of [value]
  (if (= value null-marker) "null"
      (= (type value) "boolean") "boolean"
      (= (type value) "number") "number"
      (= (type value) "string") "string"
      (array? value) (let [members []] (rawset members array-marker true)
                       (for [index 1 (# value)] (table.insert members (shape-of (. value index)))) {:sequence members})
      (= (type value) "table") (let [mapping {}]
                                (each [_ key (ipairs (sorted-keys value))] (tset mapping key (shape-of (. value key)))) {:mapping mapping})
      (error (.. "unsupported YAML value type " (type value)))))

(fn value-kind [value]
  (if (= value null-marker) "null" (array? value) "sequence" (= (type value) "table") "mapping" (type value)))

(fn read-file [path]
  (let [file (assert (io.open path "rb")) text (file:read "*a")] (file:close) text))

(fn frontmatter [text]
  (if (not (string.match text "^%-%-%-\r?\n")) {:yaml nil :error "no-opening-frontmatter"}
      (let [(start finish body) (string.find text "^%-%-%-\r?\n(.-)\n%-%-%-%s*\n")]
        (if start {:yaml body :error nil} {:yaml nil :error "unterminated-frontmatter"}))))

(fn files-under [root]
  (let [exists (os.execute (.. "test -d " (shell-quote root)))]
    (if (not (or (= exists true) (= exists 0))) nil
        (let [raw (run (.. "LC_ALL=C find " (shell-quote root) " -type f -name '*.md' -print0 | LC_ALL=C sort -z")) paths []]
          (string.gsub raw "[^\0]+" (fn [path] (table.insert paths path))) paths))))

(fn sha256 [text]
  (let [path (os.tmpname) file (assert (io.open path "wb"))]
    (file:write text) (file:close)
    (let [hash (string.match (run (.. "shasum -a 256 " (shell-quote path))) "^(%x+)")]
      (os.remove path) hash)))

(fn parse-yaml-blocks [blocks]
  ;; This bridge receives only Fennel-framed YAML input and returns only parsed values.
  (let [directory (.. (os.tmpname) "-blocks")
        created (os.execute (.. "mkdir " (shell-quote directory)))]
    (assert (or (= created true) (= created 0)))
    (let [manifest (.. directory "/manifest") listing (assert (io.open (.. directory "/manifest") "wb"))]
      (each [index block (ipairs blocks)]
        (let [path (.. directory "/" index ".yaml") file (assert (io.open path "wb"))]
          (file:write block) (file:close) (listing:write path "\n")))
      (listing:close)
      (let [program "use strict; use warnings; use YAML::XS qw(LoadFile); use JSON::PP; $YAML::XS::Boolean='JSON::PP'; my $m=shift; open my $in, '<:raw', $m or die $!; my $j=JSON::PP->new->canonical->utf8; while (<$in>) { chomp; my $v=eval { LoadFile($_) }; if ($@) { print qq{E\\t},$j->encode(\"$@\"),qq{\\n}; } else { print qq{V\\t},$j->encode($v),qq{\\n}; } }"
            output (run (.. "perl -MYAML::XS -MJSON::PP -e " (shell-quote program) " -- " (shell-quote manifest))) results []]
        (string.gsub output "[^\n]+" (fn [line] (table.insert results line)))
        (run (.. "rm -rf " (shell-quote directory))) results))))

(fn field-entry [index path record value]
  (let [entry (or (. index path) {:field_path path :presence_count 0 :record_kinds {} :observed_value_kinds {}
                                  :concrete_evidence {:path (. record :path) :sha256 (. record :sha256) :value value :shape (shape-of value)}})]
    (tset entry :presence_count (+ (. entry :presence_count) 1))
    (tset (. entry :record_kinds) (or (. record :record_kind) "untyped") true)
    (tset (. entry :observed_value_kinds) (value-kind value) true) (tset index path entry)))

(fn walk-fields [index record value path]
  (when path (field-entry index path record value))
  (if (array? value) (for [position 1 (# value)] (walk-fields index record (. value position) (.. path "[]")))
      (= (type value) "table") (each [_ key (ipairs (sorted-keys value))]
                                  (walk-fields index record (. value key) (if path (.. path "." key) key)))))

(fn set-to-array [labels] (let [result []] (rawset result array-marker true) (each [_ key (ipairs (sorted-keys labels))] (table.insert result key)) result))

(fn field-index [records]
  (let [index {}]
    (each [_ record (ipairs records)] (when (. record :frontmatter) (walk-fields index record (. record :values) nil)))
    (let [paths []]
      (rawset paths array-marker true)
      (each [_ path (ipairs (sorted-keys index))]
        (let [entry (. index path)]
          (tset entry :record_kinds (set-to-array (. entry :record_kinds)))
          (tset entry :observed_value_kinds (set-to-array (. entry :observed_value_kinds)))
          (table.insert paths entry))) paths)))

(fn main [args]
  (var offset 1) (var index-path nil)
  (when (= (. args offset) "--field-index") (set index-path (. args (+ offset 1))) (set offset (+ offset 2)))
  (when (< (- (# args) offset) 1) (error "usage: fennel inventory-frontmatter.fnl [--field-index INDEX.json] OUTPUT.json ROOT..."))
  (let [output-path (. args offset) roots [] candidates [] records []]
    (rawset roots array-marker true) (rawset candidates array-marker true) (rawset records array-marker true)
    (for [position (+ offset 1) (# args)]
      (let [root (. args position)]
        (table.insert roots root)
        (let [paths (files-under root)]
          (if (not paths) (table.insert records {:path root :sha256 null-marker :frontmatter false :error "missing-root"})
              (each [_ path (ipairs paths)]
                (let [text (read-file path) hash (sha256 text) framing (frontmatter text) yaml (. framing :yaml)]
                  (if yaml (table.insert candidates {:path path :sha256 hash :yaml yaml})
                      (table.insert records {:path path :sha256 hash :frontmatter false :error (. framing :error)}))))))))
    (let [blocks []]
      (rawset blocks array-marker true) (each [_ candidate (ipairs candidates)] (table.insert blocks (. candidate :yaml)))
      (let [parsed (parse-yaml-blocks blocks)]
        (each [position candidate (ipairs candidates)]
          (let [line (. parsed position) kind (string.sub line 1 1) payload (string.sub line 3)]
            (if (= kind "E") (table.insert records {:path (. candidate :path) :sha256 (. candidate :sha256) :frontmatter false :error (.. "YAML::XS: " (json-decode payload))})
                (let [value (json-decode payload)]
                  (if (or (not (= (type value) "table")) (array? value))
                      (table.insert records {:path (. candidate :path) :sha256 (. candidate :sha256) :frontmatter false :error "non-mapping-frontmatter"})
                      (let [record {:path (. candidate :path) :sha256 (. candidate :sha256) :frontmatter true :keys (sorted-keys value) :shapes (shape-of value) :values value}]
                        (when (= (type (. value "record_type")) "string") (tset record :record_kind (. value "record_type")))
                        (table.insert records record))))))))
    (table.sort records (fn [left right] (< (. left :path) (. right :path))))
    (let [file (assert (io.open output-path "wb"))]
      (file:write (.. (json-encode {:roots roots :records records}) "\n")) (file:close))
    (when index-path
      (let [index-file (assert (io.open index-path "wb"))]
        (index-file:write (.. (json-encode {:index_version "2" :normalization "Arrays use [] at every member position; containers and null, false, and empty values are indexed as present." :parser_inventory "same-invocation inventory output" :field_paths (field-index records)}) "\n"))
        (index-file:close))))))

(main arg)
