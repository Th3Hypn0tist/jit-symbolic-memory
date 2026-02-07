# MVP AI CLI (Codex-style)

Minimal CLI + API that can talk to **any AI provider** via adapters, and supports:
- add/get/update/list records
- ask an AI using selected records as context

## Quickstart

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt

# Start API
uvicorn api:app --reload

# In another terminal:
python cli.py add rule "Store semantics. Compute meaning. Never confuse the two."
python cli.py add db "SQL stores facts + canonical semantics. No interpretations."
python cli.py ask "Summarize in 2 sentences." --keys rule,db
```

## Provider routing

Environment defaults (API side):
- `AI_PROVIDER` = `ollama` or `openai_compat`
- `AI_MODEL` = provider model id
- `AI_BASE_URL` = provider base url
- `AI_API_KEY` = bearer key (openai_compat)

CLI can override per call:
- `--provider`, `--model`, `--base-url`, `--api-key`
