# providers.py
import requests
from typing import Dict, List

class ProviderError(RuntimeError):
    pass

def chat(provider: str, model: str, messages: List[Dict[str, str]], base_url: str, api_key: str = "") -> str:
    provider = (provider or "").lower()

    if provider == "ollama":
        url = base_url.rstrip("/") + "/api/chat"
        payload = {"model": model, "messages": messages, "stream": False}
        r = requests.post(url, json=payload, timeout=120)
        if r.status_code != 200:
            raise ProviderError(f"Ollama error {r.status_code}: {r.text}")
        data = r.json()
        return (data.get("message") or {}).get("content", "").strip()

    if provider in ("openai", "openai_compat", "compatible"):
        url = base_url.rstrip("/") + "/v1/chat/completions"
        headers = {"Content-Type": "application/json"}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        payload = {"model": model, "messages": messages}
        r = requests.post(url, headers=headers, json=payload, timeout=120)
        if r.status_code != 200:
            raise ProviderError(f"OpenAI-compatible error {r.status_code}: {r.text}")
        data = r.json()
        return data["choices"][0]["message"]["content"].strip()

    raise ProviderError(f"Unknown provider: {provider}")
