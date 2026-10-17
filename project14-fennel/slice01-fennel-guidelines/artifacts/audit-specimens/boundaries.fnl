;; Independent assertions addressing prose not fully exercised by rule pairs.
(local fennel (require :fennel))
;; lambda is non-nil checking, rather than truth, type or exact-arity checking.
(lambda accept [x ?y] (values x ?y))
(assert (= false (accept false)))
(assert (= 4 (accept 4 nil :ignored)))
(let [(ok reason) (pcall accept nil)]
  (assert (= false ok))
  (assert (string.find reason "Missing argument x" 1 true)))
;; Position adjusts multiple returns; pick-values can add explicit nil values.
(fn results [] (values 1 nil 3))
(assert (= 4 (select "#" :prefix (results))))
(assert (= 2 (select "#" (results) :suffix)))
(let [stored [(results)]] (assert (= 1 (. stored 1))) (assert (= nil (. stored 2))) (assert (= 3 (. stored 3))))
(assert (= 5 (select "#" (pick-values 5 (results)))))
;; Repeated, nil-accepting and pinned pattern names are different contracts.
(assert (= :hit (case nil ?value :hit _ :miss)))
(assert (= :miss (case nil value :hit _ :miss)))
(assert (= :hit (case nil _value :hit)))
(assert (= :hit (case [false false] [v v] :hit _ :miss)))
(assert (= :miss (case [1 2] [v v] :hit _ :miss)))
(let [expected false]
  (assert (= :hit (case false (where (= expected)) :hit _ :miss))))
(assert (= :hit (case [1 2 3] [a b] :hit _ :miss)))
;; case-try normal values short-circuit and preserve failure returns without catch.
(assert (= 2 (select "#" (case-try (values nil :reason) value value))))
(assert (= nil (case-try (values nil :reason) value value (catch :other :caught))))
(let [(ok reason) (pcall (fn [] (case-try (error :raised) v v (catch _ :caught))))]
  (assert (= false ok))
  (assert (string.find reason :raised 1 true)))
;; Resource close-on-error and success preserve all result values, including nils.
(let [closed []
      a {:close (fn [_self] (table.insert closed :a))}
      b {:close (fn [_self] (table.insert closed :b))}
      n (select "#" (with-open [x a y b] (values :value nil nil)))]
  (assert (= 3 n))
  (assert (= 2 (length closed))))
;; A nil literal in AST is a symbol. A final nested splice preserves all bodies.
(macro ast-nil? [form]
  (assert-compile (= 3 (length form)) "bad AST cardinality" form)
  (assert-compile (sym? (. form 2)) "nil is not a symbol" form)
  (assert-compile (= :nil (tostring (. form 2))) "bad nil symbol" form)
  true)
(assert (ast-nil? [1 nil 3]))
(macro run-and-return [result & body]
  `(do (do ,(unpack body)) ,result))
(var effects [])
(assert (= 99 (run-and-return 99 (table.insert effects 1) (table.insert effects 2))))
(assert (= "1,2" (table.concat effects ",")))
;; Macrodebug expands during compile and does not execute the runtime expression.

;; API default compile is permissive; explicit globals enforce boundary.
(assert (= :string (type (fennel.compileString "(not-declared 1)"))))
(let [(ok err) (pcall fennel.compileString "(not-declared 1)" {:allowedGlobals []})]
  (assert (= false ok))
  (assert (string.find (tostring err) "unknown identifier: not-declared" 1 true)))
(print :boundaries-ok)
