# cli.py
import argparse
import requests

DEFAULT_API = "http://127.0.0.1:8000"

def main():
    ap = argparse.ArgumentParser(prog="mvp-ai")
    ap.add_argument("--api", default=DEFAULT_API)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add")
    p_add.add_argument("key")
    p_add.add_argument("value")
    p_add.add_argument("--meta", default="")

    p_get = sub.add_parser("get")
    p_get.add_argument("key")

    p_upd = sub.add_parser("update")
    p_upd.add_argument("key")
    p_upd.add_argument("--value", default=None)
    p_upd.add_argument("--meta", default=None)

    p_ls = sub.add_parser("list")
    p_ls.add_argument("--limit", type=int, default=50)

    p_ask = sub.add_parser("ask")
    p_ask.add_argument("prompt")
    p_ask.add_argument("--keys", default="", help="comma-separated record keys to include")
    p_ask.add_argument("--provider", default=None)
    p_ask.add_argument("--model", default=None)
    p_ask.add_argument("--base-url", dest="base_url", default=None)
    p_ask.add_argument("--api-key", dest="api_key", default=None)

    args = ap.parse_args()
    base = args.api.rstrip("/")

    if args.cmd == "add":
        r = requests.post(f"{base}/records", json={"key": args.key, "value": args.value, "meta": args.meta})
        r.raise_for_status()
        print(r.text)
        return

    if args.cmd == "get":
        r = requests.get(f"{base}/records/{args.key}")
        r.raise_for_status()
        print(r.text)
        return

    if args.cmd == "update":
        payload = {}
        if args.value is not None:
            payload["value"] = args.value
        if args.meta is not None:
            payload["meta"] = args.meta
        r = requests.patch(f"{base}/records/{args.key}", json=payload)
        r.raise_for_status()
        print(r.text)
        return

    if args.cmd == "list":
        r = requests.get(f"{base}/records", params={"limit": args.limit})
        r.raise_for_status()
        print(r.text)
        return

    if args.cmd == "ask":
        keys = [k.strip() for k in args.keys.split(",") if k.strip()] if args.keys else None
        payload = {"prompt": args.prompt, "keys": keys}
        if args.provider:
            payload["provider"] = args.provider
        if args.model:
            payload["model"] = args.model
        if args.base_url:
            payload["base_url"] = args.base_url
        if args.api_key:
            payload["api_key"] = args.api_key

        r = requests.post(f"{base}/ask", json=payload)
        r.raise_for_status()
        print(r.json().get("response", ""))
        return

if __name__ == "__main__":
    main()
