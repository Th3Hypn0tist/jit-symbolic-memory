# api.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

import store
import providers

app = FastAPI(title="AI CLI MVP API")
store.init_db()

class RecordIn(BaseModel):
    key: str
    value: str
    meta: Optional[str] = ""

class RecordUpdate(BaseModel):
    value: Optional[str] = None
    meta: Optional[str] = None

class AskIn(BaseModel):
    prompt: str
    provider: str = os.getenv("AI_PROVIDER", "ollama")
    model: str = os.getenv("AI_MODEL", "llama3.1:8b-instruct-q4_K_M")
    base_url: str = os.getenv("AI_BASE_URL", "http://127.0.0.1:11434")
    api_key: str = os.getenv("AI_API_KEY", "")
    keys: Optional[List[str]] = None

@app.post("/records")
def add_record(rec: RecordIn):
    try:
        return store.add_record(rec.key, rec.value, rec.meta or "")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/records/{key}")
def get_record(key: str):
    out = store.get_record(key)
    if not out:
        raise HTTPException(status_code=404, detail="not found")
    return out

@app.patch("/records/{key}")
def patch_record(key: str, upd: RecordUpdate):
    out = store.update_record(key, value=upd.value, meta=upd.meta)
    if not out:
        raise HTTPException(status_code=404, detail="not found")
    return out

@app.get("/records")
def list_records(limit: int = 50):
    return store.list_records(limit=limit)

@app.post("/ask")
def ask(req: AskIn):
    ctx_lines = []
    used = []
    if req.keys:
        for k in req.keys:
            r = store.get_record(k)
            if r:
                used.append(k)
                ctx_lines.append(f"- {r['key']}: {r['value']}")

    system = (
        "You are a stateless assistant. Use only provided context. "
        "If context is insufficient, say what is missing. Do not hallucinate."
    )

    messages = [{"role": "system", "content": system}]
    if ctx_lines:
        messages.append({"role": "user", "content": "Context records:\n" + "\n".join(ctx_lines)})
    messages.append({"role": "user", "content": req.prompt})

    try:
        text = providers.chat(
            provider=req.provider,
            model=req.model,
            messages=messages,
            base_url=req.base_url,
            api_key=req.api_key or "",
        )
        return {"response": text, "used_keys": used}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
