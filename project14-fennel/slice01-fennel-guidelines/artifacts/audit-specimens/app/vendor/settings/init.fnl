(fn parse [text]
  "Parse boolean assignments; return a fresh map or nil and an error message."
  (let [result {}
        problem {:message nil}]
    (each [line (string.gmatch text "[^\n]+") &until problem.message]
      (let [(key token) (string.match line "^%s*([%w_-]+)%s*=%s*(%S+)%s*$")]
        (if (= nil key)
            (set problem.message (.. "invalid assignment: " line))
            (not= nil (. result key))
            (set problem.message (.. "duplicate option: " key))
            (= token :true)
            (set (. result key) true)
            (= token :false)
            (set (. result key) false)
            (set problem.message (.. "invalid boolean: " token)))))
    (if problem.message (values nil problem.message) result)))

(fn render [options]
  "Render options in deterministic key order."
  (let [keys (icollect [key _value (pairs options)] key)]
    (table.sort keys)
    (table.concat (icollect [_ key (ipairs keys)]
                    (.. key "=" (tostring (. options key))))
                  "\n")))

{: parse : render}
