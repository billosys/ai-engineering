# vLLM-Metal and LibreChat on the M2 Ultra Mac Pro

Date: 2026-09-22

Status: source-checked installation and commissioning draft; not executed on the target

Companion: [Local coding model experiment protocol](./local-coding-model-experiment-protocol.md)

## Purpose and authority

Set up local inference for bounded coding assignments, including the
collaboration-framework's required-reading and contract-readback obligations.
The Operator approved these two standalone documents in the ai-engineering
planning worktree on 2026-09-22. This is not a new project/arc/slice, an issued
CC prompt, or authorization to call unrun checks successful.

The assistant researched upstream documentation and inspected the local
LibreChat example configuration and schema. Installation, model downloads,
service changes, model evaluation, and target-machine acceptance have not run.
Commands below are instructions for the target environment, not execution logs.

## 1. Confirmed hardware and deployment facts

| Item | Baseline | Evidence |
| --- | --- | --- |
| Inference host | Mac Pro, Apple M2 Ultra | Operator's order information |
| CPU / GPU / Neural Engine | 24 / 76 / 32 cores | Operator's order information |
| Unified memory | 192 GB | Operator |
| Installed storage | 8 TB SSD; free space not yet measured | Operator |
| macOS | 15.7; exact patch/build to capture at commissioning | Operator |
| LibreChat | Installed on both Mac Pro and MacBook Pro | Operator |
| Current assistant host | M1 Max MacBook Pro, 64 GB, macOS 15.7.9 | Local inspection on 2026-09-22 |
| Each LibreChat deployment mode | Native versus Docker remains unspecified | Open |
| Target network identity | Private hostname/address remains unspecified | Open |

Run inference on the Mac Pro. Either LibreChat installation can use it; a
second model server on the MacBook is not needed. Run one scored experiment at
a time across both clients so their requests do not compete. The Neural Engine
core count is inventory information, not a claimed accelerator for this setup.

The current vLLM-Metal requirements are Apple Silicon, macOS 15 or newer, and
native arm64 Python 3.12. The stated target satisfies the hardware/OS criteria;
capture the actual runtime architecture during setup. [S1]

## 2. Model selection

| Condition | Exact repository ID | Published weight size | Use |
| --- | --- | --- | --- |
| N8 | `mlx-community/Qwen3-Coder-Next-8bit` | 84.7 GB | First quality candidate [S5] |
| N4 | `mlx-community/Qwen3-Coder-Next-4bit` | 44.8 GB | Quantization comparison [S6] |
| C30 | `mlx-community/Qwen3-Coder-30B-A3B-Instruct-8bit` | 32.4 GB | Optional smaller challenger [S7] |

Sizes are model weights, not total memory consumption. Cache, temporary
buffers, macOS, LibreChat, containers, and build processes also consume memory.
Load one candidate at a time. Start with N8 because the stated capacity makes
it plausible; retain N4 if measured quality is comparable and its operational
cost is preferable. This is a hypothesis, not a measured recommendation.

Qwen3-Coder-Next has 80B total parameters, about 3B active per token, a native
262,144-token context, and non-thinking output. There is no `xhigh` equivalent
to set here. Use the Operator's luna xhigh workflow as a measured reference.
Start with a much smaller context for commissioning. Qwen recommends
temperature 1.0, top-p 0.95, and top-k 40. [S4]

The Metal support table includes the Qwen3-Next family. Family support does
not establish that this exact quantized checkpoint and full agent stack work
on this machine; the commissioning checks below establish that separately.
Hybrid prefix-cache support is marked experimental in the inspected table.
Keep default cache behavior recorded and unchanged within comparisons. [S3]

## 3. Architecture and file visibility

```text
Mac Pro LibreChat -----------+
                            +--> Mac Pro vLLM-Metal --> MLX --> M2 Ultra GPU
MacBook Pro LibreChat -------+

Each LibreChat Agent --> its configured filesystem MCP process --> task packet
Operator test runner --> disposable checkout --> compiler/tests --> saved logs
```

The inference server receives messages and tool descriptions. It does not
read a repository merely because a message contains a path. LibreChat executes
the tool call and sends the tool result back to the model.

File tools run in the LibreChat backend's environment, independently of where
inference runs. A MacBook LibreChat backend therefore needs its own copy of the
packet, a mounted copy, or a deliberately configured remote tool service.
Pointing it at the Mac Pro inference URL does not expose Mac Pro files.

For the first trials, use an immutable packet copy and have the model return
a unified diff. The Operator applies it in a disposable checkout and runs
fixed tests. This isolates instruction intake and output quality. An autonomous
edit/build/test loop requires an additional execution tool and a separate
commissioning pass; filesystem MCP alone is not a shell or compiler.

## 4. Capture the target baseline

Run on the Mac Pro, not the MacBook:

```bash
uname -m
sw_vers
system_profiler SPHardwareDataType
df -h "$HOME"
sysctl vm.swapusage
```

Expected architecture: `arm64`. Record the OS build and actual free storage.
Do not include device serial numbers or UUIDs in shared evidence. Allow room
for both selected checkpoints, package caches, and experiment workspaces;
installed SSD capacity is not available capacity.

Create a dedicated operator-chosen setup/evidence directory on the Mac Pro.
Run the following installation commands there, outside a vLLM-Metal source
checkout. No directory on the remote Mac has been created by this document.

## 5. Install and record the runtime

```bash
curl -fsSL \
  https://raw.githubusercontent.com/vllm-project/vllm-metal/main/install.sh \
  -o install-vllm-metal.sh

less install-vllm-metal.sh
shasum -a 256 install-vllm-metal.sh

bash install-vllm-metal.sh --stable

source "$HOME/.venv-vllm-metal/bin/activate"

python -c 'import platform, sys; print(platform.machine()); print(sys.version)'
uv pip freeze > runtime-packages.txt
vllm serve --help > vllm-serve-help.txt
```

Use the supported installer rather than substituting a generic `pip install
vllm` or CUDA Docker recipe. The current installer obtains the matching core
and Metal wheels; its default channel is development, hence explicit
`--stable` here. [S1]

The source checked for this draft was vLLM-Metal `v0.29.0`; its metadata selects
vLLM `v0.29.0`. Running the command later may select a newer release. Preserve
installation output, installer hash, selected wheel URLs, package inventory,
and any installation failure. A saved installer and `pip freeze` alone are
not a complete reproducible wheel archive. Freeze the working environment
through the experiment; archive dependencies before trying an upgrade. [S2]

The inspected installer takes a source-build path if it finds its local
`scripts/lib.sh`; this is why these commands belong outside a source checkout.
Do not run this over an existing experiment environment without first retaining
its version record and a recovery path. [S2]

Gate: native arm64 Python 3.12, successful imports/startup, and captured package
versions. Repair architecture or install failures before downloading large models.

## 6. Pin the checkpoint and start the server

In the activated environment:

```bash
export MODEL_ID='mlx-community/Qwen3-Coder-Next-8bit'

export MODEL_REV="$(
  python - <<'PY'
import os
from huggingface_hub import HfApi
print(HfApi().model_info(os.environ["MODEL_ID"]).sha)
PY
)"

test -n "$MODEL_REV"
printf '%s\n%s\n' "$MODEL_ID" "$MODEL_REV" > model-revision.txt

export MODEL_PATH="$(
  python - <<'PY'
import os
from huggingface_hub import snapshot_download
print(snapshot_download(
    repo_id=os.environ["MODEL_ID"],
    revision=os.environ["MODEL_REV"],
))
PY
)"

test -d "$MODEL_PATH"
printf '%s\n' "$MODEL_PATH" > model-snapshot-path.txt

export VLLM_API_KEY="$(openssl rand -hex 32)"

vllm serve "$MODEL_PATH" \
  --served-model-name local-coder \
  --host 127.0.0.1 \
  --port 8000 \
  --api-key "$VLLM_API_KEY" \
  --max-model-len 32768 \
  --max-num-seqs 1 \
  --gpu-memory-utilization 0.70 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder
```

Run the steps interactively; stop on a failed revision lookup or download rather
than continuing with an empty revision or path. Retain the key privately for both LibreChat
configurations and later server restarts. Do not regenerate it on each restart
unless intentionally rotating the clients' credentials too.

The model revision is resolved before downloading and retained with the
condition identity. Serve the resulting local snapshot to avoid relying on
revision propagation through backend loaders. Do not edit the cached snapshot.
Hugging Face supports revision-pinned snapshot retrieval. [S8]

The launch settings are proposed commissioning values, not a benchmark result.
On the documented default paged-KV path, the Metal `auto` memory budget uses
`--gpu-memory-utilization`. Leave unrelated tuning variables unset and record
effective settings from the startup log. If allocation fails, first identify
whether weights, cache reservation, or another process is responsible. Do not
blindly increase the memory fraction. [S9]

The checked vLLM release maps `qwen3_coder` and `qwen3_xml` to the same parser.
Use the installed version's supported parser; do not treat textual XML in a
response as a successfully parsed tool call. [S10]

Wait for the readiness message. Capture load time, startup warnings, and memory
pressure. Do not infer request readiness from a listening port alone.

## 7. Commission the API and tool-call transport

In another terminal, make the same key available privately:

```bash
curl --fail-with-body http://127.0.0.1:8000/v1/models \
  -H "Authorization: Bearer $VLLM_API_KEY"

curl --fail-with-body http://127.0.0.1:8000/v1/chat/completions \
  -H "Authorization: Bearer $VLLM_API_KEY" \
  -H 'Content-Type: application/json' \
  --data '{
    "model": "local-coder",
    "messages": [{"role":"user","content":"Return exactly: connection established"}],
    "temperature": 0,
    "max_tokens": 32
  }'
```

Expected: the model listing includes `local-coder`; the completion is valid JSON
with an assistant response. The exact-text prompt is a transport smoke check,
not a coding benchmark. Use normal study sampling for scored trials.

Next send a tool-enabled request:

```bash
curl --fail-with-body http://127.0.0.1:8000/v1/chat/completions \
  -H "Authorization: Bearer $VLLM_API_KEY" \
  -H 'Content-Type: application/json' \
  --data '{
    "model": "local-coder",
    "messages": [{"role":"user","content":"Read /workspace/packet/cc-prompt.md using read_text_file before answering."}],
    "tools": [{
      "type":"function",
      "function": {
        "name":"read_text_file",
        "description":"Read a UTF-8 file from an allowed absolute path.",
        "parameters": {
          "type":"object",
          "properties":{"path":{"type":"string"}},
          "required":["path"],
          "additionalProperties":false
        }
      }
    }],
    "tool_choice":"auto",
    "temperature":1.0,
    "top_p":0.95,
    "top_k":40,
    "max_tokens":1024
  }'
```

Expected: an assistant `tool_calls` entry naming `read_text_file`, with
parseable arguments and the requested path. This curl request defines a tool
schema but does not implement or execute the tool. Complete the actual read
and follow-up model response through LibreChat in section 11. If this probe
fails, preserve it and diagnose parser/template/model behavior before coding.

## 8. Connect both LibreChat installations

First get the Mac Pro's local LibreChat connection working; then connect the
MacBook client. Choose the address from the backend's perspective:

| LibreChat backend | vLLM base URL | Server binding |
| --- | --- | --- |
| Mac Pro, native | `http://127.0.0.1:8000/v1` | Initial loopback bind |
| Mac Pro, Docker Desktop | `http://host.docker.internal:8000/v1` | Test from the container; use a reachable host bind if loopback fails |
| MacBook, native or Docker, direct private network | `http://MAC_PRO_PRIVATE_ADDRESS:8000/v1` | Bind vLLM to the Mac Pro's private interface, or `0.0.0.0` with access restricted to the intended private clients |
| MacBook, native, SSH tunnel | `http://127.0.0.1:18000/v1` | Keep Mac Pro loopback bind |

`MAC_PRO_PRIVATE_ADDRESS` and the SSH target below are placeholders. Docker
Desktop provides `host.docker.internal` for reaching the Docker host. It does
not mean the other Mac; on the MacBook it refers to the MacBook. [S12]

Optional native-MacBook tunnel, if SSH access to the Mac Pro is already set up:

```bash
ssh -N -o ExitOnForwardFailure=yes \
  -L 127.0.0.1:18000:127.0.0.1:8000 \
  MAC_PRO_SSH_TARGET
```

Keep that connection running. Docker access to a host-loopback tunnel is
deployment-dependent: test from the container and do not assume this native
recipe works unchanged. The direct private-network route is the explicit
alternative. Keep API authentication for every route; do not publish port 8000
through a public router. Test the chosen URL from each backend environment.

In each installation, merge this endpoint entry into the existing
`librechat.yaml`, selecting the appropriate `baseURL` above:

```yaml
endpoints:
  custom:
    - name: "LocalCoder"
      apiKey: "${LOCAL_CODER_API_KEY}"
      baseURL: "http://host.docker.internal:8000/v1"
      models:
        default: ["local-coder"]
        fetch: false
      titleConvo: false
      summarize: false
      modelDisplayLabel: "Local Coder"
      addParams:
        temperature: 1.0
        top_p: 0.95
        top_k: 40
        max_tokens: 4096
```

This is a fragment: preserve the existing top-level configuration version,
other endpoints, and existing settings. Do not create duplicate `endpoints`
keys. Add `LOCAL_CODER_API_KEY` to that deployment's private environment using
the server's existing key. Static model selection and disabled title generation
reduce incidental requests during trials. [S11]

For Docker Compose, merge the configuration mount into the existing override:

```yaml
services:
  api:
    volumes:
      - ./librechat.yaml:/app/librechat.yaml:ro
```

Use the actual deployment directory and Compose file set:

```bash
docker compose config --quiet
docker compose up -d --no-deps --force-recreate api
docker compose logs --tail=100 api
```

The local inspected checkout uses service `api`; verify the Mac Pro deployment
before substituting this command into its procedures. Native deployments should
restart their existing process/service using its established launcher.

Verify the model choice and effective request parameters in each client. Do not
assume Agent Builder settings, endpoint `addParams`, and UI defaults combine
as intended without observing the request. Any token limit must leave room for
instructions, tool schemas, results, history, and output within the server cap.

## 9. Configure access to the task packet

Choose one LibreChat deployment for the scored pilot; the other is a separately
commissioned client, not an additional concurrent trial runner.

Prepare a task packet with preserved relative paths. Include the active prompt,
required plans and ledger, bound guide sections, coding examples, and source
inputs. Exclude expected patches, evaluator-only tests, other trial outputs,
and unrelated workspaces. Record transformations from original absolute paths
in the packet manifest. Keep originals unchanged.

For Docker, merge a read-only mount into the existing override, replacing the
host placeholder with an existing absolute directory:

```yaml
services:
  api:
    volumes:
      - /ABSOLUTE/HOST/PACKET:/workspace/packet:ro
```

The reference filesystem MCP server is a read/write server; the mount and
selected tools make this particular packet read-only. Select reading/listing
tools only. For native deployment, select only read tools and use a dedicated
packet copy; tool selection is not an OS filesystem sandbox. [S14]

Resolve an exact filesystem-server version during commissioning in the
backend environment, record it, and replace `PINNED_VERSION` below. For example,
`npm view @modelcontextprotocol/server-filesystem version` discovers the current
published version; it is not a pin until that value is saved in the config.
Verify Node/npx availability and warm the package cache before timing trials.

```yaml
mcpServers:
  experiment-files:
    type: stdio
    command: npx
    args:
      - "-y"
      - "@modelcontextprotocol/server-filesystem@PINNED_VERSION"
      - "/workspace/packet"
```

For native LibreChat, replace `/workspace/packet` with its actual packet path
and update the trial entry prompt accordingly. Restart LibreChat and confirm
MCP tool discovery. Configuration is evaluated in the backend environment. [S13]

The reference tool has full-file reads and head/tail options. It is not a
general line-range reader. Keep initial required files small enough for a
lossless full read. If a full result is truncated and available tools cannot
recover all omitted content, stop that trial as blocked; commission a range
reader or an author-defined, lossless packet partition before retrying under
a new recorded configuration. A tail read alone does not recover an omitted
middle. [S14]

## 10. Create the LibreChat Agent

Use Agent Builder, select `LocalCoder` / `local-coder`, and attach the configured
filesystem MCP tools. Disable unrelated tools, automatic memory, and retrieval
for the controlled trials. RAG snippets do not establish complete loading of a
required document. Agent settings and enabled tools must be saved per condition.
LibreChat exposes model parameters and MCP tool selection in Agent Builder. [S15]

Use this intake instruction, adapting only the visible packet root:

> The active assignment is `/workspace/packet/cc-prompt.md`. Read it through
> the filesystem tool. Follow its required-reading manifest before dependent
> work. Resolve relative links from the document containing them. Load complete
> required text, including code blocks and appendices; recover truncated output.
> Record the loaded extents and give a source-cited contract readback. Distinguish
> required-full, required-section, required-data, conditional, and reference-only
> material. If required material is unavailable or contradictory, report the
> exact blocker and stop dependent work. Do not claim a file was read unless
> its contents were returned by a tool. Do not claim tests ran without execution
> evidence. In this patch-output trial, return a unified diff and explicitly
> identify checks the operator must run; no execution tool is available.

This instruction supplements the full task packet. It does not replace the
framework, task-specific design, coding examples, or domain guidance. The
author must budget the packet and enumerate normative dependencies. [L1]

## 11. Commission the complete path

Record each check separately for the Mac Pro and MacBook LibreChat clients:

1. Backend can reach `/v1/models` with authentication.
2. A normal response renders successfully.
3. The Agent emits a structured filesystem call.
4. The tool executes against the actual packet and returns its contents.
5. The model's follow-up response uses those returned contents correctly.
6. A nested relative link resolves to the intended file.
7. Missing required input produces an honest blocker.
8. Streaming works for tool-call arguments, tool results, and the final answer.
9. Actual tool-result and context truncation behavior is observable.
10. The transcript/export preserves enough raw evidence for the protocol.

Check 7 here is a smoke test; the repeated scored missing-file control is a
separate experiment. An application export that omits tool results is not
sufficient evidence. Establish a backend trace/export route before scoring;
retain actual content and call identifiers with credentials removed. If that
route cannot capture what the model received, mark evidence completeness
blocked rather than inferring reads from a file list.

## 12. Operate, recover, and tune

| Symptom | First discriminating check |
| --- | --- |
| Import/install failure | Python architecture/version and matched wheel pair |
| Model load failure | Exact model revision, supported architecture, server log |
| Allocation failure or swap growth | Other processes, cache allocation, context cap, weight footprint |
| Client cannot connect | Probe from the backend/container, verify bind address and URL |
| Authentication failure | Client/server key agreement without logging the secret |
| Model not found | Served alias is exactly `local-coder` |
| Tool call appears as plain text | Chat template, enabled tools, parser, raw response |
| File not found | Path from the MCP process's environment, mount and relative-link root |
| Correct read claim but wrong output | Tool content trace, contract readback, behavioral oracle |
| Cut-off answer | Finish reason, output cap, context budget, client timeout |

Change one setting at a time during diagnosis and record it. Stop the foreground
server with Ctrl-C; keep evidence and downloaded checkpoints. Restore prior
LibreChat settings/mounts if abandoning the trial. No uninstall, global reset,
or replacement of existing Ollama configuration is required for this pilot.

Once 32K works, qualify 64K separately with a real packet and measured memory
pressure. Do not advertise the model's native maximum as the machine's tested
capacity. Time cold load, warm prefill, and full task completion separately.
Token throughput is secondary to correct completion and operator effort.

For repeat use, preserve the proven launch command and environment before
adding service management. No launchd service is created by this draft.

## 13. Acceptance and remaining work

Ready for the experiment only when the exact model/runtime combination starts,
the complete LibreChat tool loop works, evidence capture is adequate, and the
selected task packet fits without silent truncation. This remains pending.

Remaining deployment facts: each LibreChat's native/Docker mode and version,
the Mac Pro network identity, current free storage, and the chosen packet and
evidence locations on the execution host. They can be filled during setup
without changing this approved planning-document location.

No conclusion about coding quality, luna parity, or autonomous CC suitability
is supported until the companion protocol is executed and reviewed.

## Sources and local provenance

Upstream pages/source were checked on 2026-09-22. Mutable documentation should
be rechecked if the installed versions differ. Each citation supports only its
associated installation, model, configuration, or API fact; proposed operating
values and experimental judgments are this runbook's design choices.

- **S1:** [vLLM-Metal installation](https://docs.vllm.ai/projects/vllm-metal/en/stable/installation/).
- **S2:** [v0.29.0 installer](https://raw.githubusercontent.com/vllm-project/vllm-metal/v0.29.0/install.sh), [matched core metadata](https://raw.githubusercontent.com/vllm-project/vllm-metal/v0.29.0/.github/vllm-release-tag.commit), [release](https://github.com/vllm-project/vllm-metal/releases/tag/v0.29.0).
- **S3:** [Metal supported models](https://docs.vllm.ai/projects/vllm-metal/en/stable/supported_models/).
- **S4:** [Qwen3-Coder-Next model card](https://huggingface.co/Qwen/Qwen3-Coder-Next).
- **S5:** [MLX Next 8-bit](https://huggingface.co/mlx-community/Qwen3-Coder-Next-8bit).
- **S6:** [MLX Next 4-bit](https://huggingface.co/mlx-community/Qwen3-Coder-Next-4bit).
- **S7:** [MLX Coder 30B 8-bit](https://huggingface.co/mlx-community/Qwen3-Coder-30B-A3B-Instruct-8bit).
- **S8:** [Hugging Face revision-pinned downloads](https://huggingface.co/docs/huggingface_hub/guides/download).
- **S9:** [Metal configuration](https://docs.vllm.ai/projects/vllm-metal/en/stable/configuration/).
- **S10:** [vLLM v0.29.0 parser registry](https://raw.githubusercontent.com/vllm-project/vllm/v0.29.0/vllm/tool_parsers/__init__.py).
- **S11:** [LibreChat custom endpoints](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/custom_endpoint).
- **S12:** [Docker Desktop networking](https://docs.docker.com/desktop/features/networking/).
- **S13:** [LibreChat MCP configuration](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/mcp_servers).
- **S14:** [Reference filesystem server](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md).
- **S15:** [LibreChat Agents](https://www.librechat.ai/docs/features/agents).
- **L1:** [Required-reading and CC intake contract](../../knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md#required-reading-and-cc-intake).

Local source inspected: LibreChat checkout
`/Users/oubiwann/lab/billosys/LibreChat`, HEAD
`86c5884c0f6c7ee50409d6b7abb27c569a275621`, package version `v0.8.8-rc3`;
`librechat.example.yaml`, `docker-compose.yml`, and
`packages/data-provider/src/config.ts`. This identifies the inspected local
source, not either running deployment's image/version. The source configuration
supports the endpoint fields used above. No private environment files were read.

## Document history

- 2026-09-22: Initial standalone draft; incorporated Operator-confirmed M2 Ultra
  specifications, macOS 15.7, and LibreChat on both Macs. Target execution and
  installation remain pending.
