(let [state {:closed? false}
      handle (setmetatable {} {:__close (fn [_self _error] (set state.closed? true))})]
  (with-open [resource handle] :done)
  (assert state.closed?))
(print :native-protocol-ok)
