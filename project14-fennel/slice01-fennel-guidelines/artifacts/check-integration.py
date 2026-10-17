#!/usr/bin/env python3
"""Exercise real module/macro loading, embedding, relocation and clean AOT delivery."""
from pathlib import Path
import json
import subprocess
import tempfile

results=[]
def run(label, command, cwd, expected=0):
    r=subprocess.run(command,cwd=cwd,text=True,capture_output=True)
    results.append({'label':label,'command':command,'expected_exit':expected,'exit':r.returncode,
                    'stdout':r.stdout,'stderr':r.stderr})
    if r.returncode!=expected:
        raise RuntimeError(label+': '+r.stderr)
    return r.stdout

with tempfile.TemporaryDirectory(prefix='fennel-integration-') as tmp:
    root=Path(tmp)
    files={
        'libs/example/init.fnl':'''(local worker (require (.. ... :.worker)))
{:double worker.double}
''',
        'libs/example/worker.fnl':'''(fn double [x] (* x 2))
{: double}
''',
        'checks.fnlm':'''(fn twice [x] `(let [value# ,x] (+ value# value#)))
{: twice}
''',
        'main.fnl':'''(import-macros {: twice} :checks)
(local library (require :libs.example))
(var calls 0)
(fn next! [] (set calls (+ calls 1)) 3)
(assert (= 12 (library.double (twice (next!)))))
(assert (= 1 calls))
(with-open [file (assert (io.open "fixture.txt"))]
  (assert (= "hello" (file:read :*l))))
(print "integration-ok")
''',
        'fixture.txt':'hello\n',
        'host.lua':'''local fennel = require("fennel")
fennel.install()
fennel.dofile("main.fnl")
local code = fennel.compileString("(print (+ 1 2))", {
  filename = "example.fnl", allowedGlobals = {"print"}
})
assert(type(code) == "string")
'''}
    for name, text in files.items():
        file=root/name;file.parent.mkdir(parents=True,exist_ok=True);file.write_text(text)
    run('Fennel module and macro consumer',['fennel','main.fnl'],root)
    run('embedded Lua host',['lua','host.lua'],root)
    compiled=run('AOT bundled compile with globals checking',
                 ['fennel','--globals','','--require-as-include','--compile','main.fnl'],root)
    shipped=root/'shipped';shipped.mkdir()
    (shipped/'main.lua').write_text(compiled)
    (shipped/'fixture.txt').write_text('hello\n')
    # No .fnl or compiler library may be found by the emitted artifact.
    output=run('clean emitted artifact without loaders',
               ['lua','-e','package.path=""; package.cpath=""; dofile("main.lua")'],shipped)
    if output.strip()!='integration-ok':raise RuntimeError('wrong emitted artifact output')
    (root/'missing.fnl').write_text('(misspelled-processor 1)\n')
    run('strict AOT rejects unknown globals',['fennel','--globals','','--compile','missing.fnl'],root,1)
    run('bare AOT illustrates unchecked emission',['fennel','--compile','missing.fnl'],root)
    # Actually relocate the library, rather than only testing string concatenation.
    relocated=root/'vendor/example';relocated.parent.mkdir();(root/'libs/example').rename(relocated)
    text=(root/'main.fnl').read_text().replace(':libs.example',':vendor.example')
    (root/'main.fnl').write_text(text)
    run('relocated runtime module consumer',['fennel','main.fnl'],root)
    compiled=run('relocated AOT relative include',
                 ['fennel','--globals','','--require-as-include','--compile','main.fnl'],root)
    (shipped/'main.lua').write_text(compiled)
    run('clean relocated emitted artifact',
        ['lua','-e','package.path=""; package.cpath=""; dofile("main.lua")'],shipped)
    (root/'native-close.fnl').write_text('(let [state {:closed? false :error? false}\n      handle (setmetatable {} {:__close (fn [_self reason]\n                                          (set state.closed? true)\n                                          (set state.error? (not= nil reason)))})\n      [ok? reason] [(pcall (fn []\n                            (with-open [resource handle]\n                              (error "native read failed"))))]]\n  (assert (= false ok?))\n  (assert (string.find reason "native read failed" 1 true))\n  (assert state.closed?)\n  (assert state.error?))\n(print "native-cleanup-ok")\n')
    run('native __close cleanup on raised body error',
        ['fennel','--to-be-closed','native-close.fnl'],root)
    native=run('strict native-mode compilation',
               ['fennel','--globals','','--to-be-closed','--compile','native-close.fnl'],root)
    (root/'native-close.lua').write_text(native)
    run('emitted Lua native cleanup',['lua','native-close.lua'],root)
    (root/'native-negative.fnl').write_text('(let [handle {:close (fn [_self] nil)}]\n  (with-open [resource handle] :done))\n')
    run('native mode rejects close-only custom resources',
        ['fennel','--to-be-closed','native-negative.fnl'],root,1)
    if 'non-closable' not in results[-1]['stderr']:
        raise RuntimeError('native rejection was not the expected protocol error')
Path(__file__).with_name('integration-results.json').write_text(json.dumps(results,indent=2)+'\n')
print(f'PASS: {len(results)} integration/negative checks')
