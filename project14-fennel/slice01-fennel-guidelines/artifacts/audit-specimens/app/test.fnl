(local settings (require :vendor.settings))
(local data (assert (settings.parse "z=true\na=false")))
(assert (= false data.a))
(assert (= true data.z))
(assert (= "a=false\nz=true" (settings.render data)))
(each [_ text (ipairs [:a=maybe "a=false\na=true" "bad syntax"])]
  (case (settings.parse text)
    (nil message) (assert (= :string (type message)))
    _ (error "expected value failure")))

(assert (not= (settings.parse :a=true) (settings.parse :a=true)))
(print :settings-ok)
