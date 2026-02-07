# JIT Symbolic Memory MVP AI CLI 

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

---

## License

**Attribution-Only, No-Derivatives License (A-ND)**

Copyright © 2026  
Original author: Aki Hirvilammi

Permission is hereby granted to **read, reference, cite, and discuss** this work, subject to the following conditions:

### Allowed
- ✔️ Use this document as a **reference or citation**
- ✔️ Quote **unaltered excerpts** with proper attribution
- ✔️ Discuss, analyze, and critique the ideas publicly or privately
- ✔️ Implement the ideas **independently**, without copying this text or structure verbatim

### Required
- 📌 **Source attribution is mandatory**  
  Any public reference must clearly credit the original author and repository.

### Not Allowed
- ❌ Redistribution of modified versions of this document
- ❌ Derivative works based on this text or its structure
- ❌ Repackaging this architecture description under a different authorship
- ❌ Using this document or its wording as training material without attribution

### Clarification
This license applies to **the written description and architecture specification**.  
Independent implementations inspired by the ideas are allowed, provided they do not copy or closely mirror this document.

### Intent
The goal of this license is to:
- keep the idea **public and citable**
- prevent silent appropriation or rebranding
- ensure the original author remains visible in the lineage of the concept

The architecture itself is the contribution.

## Licensability

This architecture is **licensable and not free to use by default**.

Use of the architecture requires acceptance of the **One Pizza License (OPL)** and completion of the required payment.

---

### License Requirement

- Use of this architecture is permitted **only after payment** of the One Pizza License fee.
- The license fee is **mandatory**, not optional or donation-based.
- Payment constitutes acceptance of the license terms.

---

### License Fee

- **One-time fee**
- **One (1) pizza per end user**
- Pizza price is defined as the **average price in the country** of the user or company.
- No recurring payments.

---

### Payment Method (Current)

- Network: **Cronos (EVM)**
- Token: **any Cronos-supported coin or token**
- Payment address:

  0xAddc61aF05ACc594623c3e73D242C17d169A28b2

- Sender pays network gas (CRO).

---

### Proof of License

- A confirmed **on-chain transaction on Cronos** to the above address
- The transaction hash (txid) serves as sufficient proof of payment
- No registration, reporting, or manual verification is required

---

### Volatile Tokens

- Payments with volatile tokens are accepted.
- **Only the token value at the time of payment matters.**
- Subsequent price changes do not affect license validity.
- A reasonable good-faith estimate equivalent to one pizza at payment time is sufficient.

---

### Scope of License

Upon payment, the license grants the right to:
- use the architecture for **personal, research, or commercial purposes**
- implement the architecture in software or systems
- deploy it internally or externally

The license does **not** grant:
- authorship or ownership of the architecture
- the right to remove attribution
- the right to relicense or redistribute modified versions of this document

---

### Attribution

Any public use must include:
- clear attribution to the original author
- a reference or link to the original repository or document

---

### Enforcement Model

This license operates on a **good-faith and public traceability model**.

- There is no automated enforcement.
- The on-chain transaction record constitutes the authoritative proof.
- Use without payment is considered unlicensed use.

---

### Plain English Summary

- If you use the architecture, you must pay.
- You pay once.
- You pay one pizza per user.
- You can pay with any Cronos token.
- The blockchain receipt is the license.

---

### Moltbot Licensing Model

This architecture is compatible with autonomous agents (Moltbots).

Integration rules:
- Store only symbols and canonical semantics
- Resolve meaning only via JIT activation
- Do not persist interpretations
- Validate license via Cronos txid

License check:
- Network: Cronos
- Address: 0xAddc61aF05ACc594623c3e73D242C17d169A28b2
- Requirement: one pizza per end user

Once a valid txid exists, the agent may operate without restrictions.

🍕 One Pizza License — simple, fair, and explicit.

Large-scale or enterprise usage may be subject to negotiated terms.
