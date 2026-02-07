# JIT Symbolic Memory Architecture for LLMs (MVP)

Stateless semantic memory effect for LLM systems  
PostgreSQL · Symbols · Just-In-Time Meaning · Ollama / LLaMA

---

## TL;DR

This repository contains an **MVP implementation** of a stateless symbolic memory architecture for LLMs.

- store facts and canonical semantics
- compute meaning only at runtime
- avoid persistent cognitive state
- keep reasoning repeatable and inspectable

This produces a **memory effect without memory**.

Use of the architecture requires acceptance of the **One Pizza License (OPL)**.

---

## Architecture Definition (Upstream)

The canonical definition of the architecture lives here:

👉 https://github.com/Th3Hypn0tist/random/blob/main/LLM-symbolic-memory.md

This repository does **not redefine** the architecture.  
It implements an MVP based on that definition.

---

## Why This Exists

Large Language Models do not have memory in the traditional sense.

Attempts to give them memory usually fail by:
- storing interpretations instead of facts
- polluting context windows
- creating hidden or drifting state
- mixing probabilistic reasoning with deterministic storage

This architecture takes the opposite approach:

**LLMs should not store meaning.  
They should compute it when needed.**

---

## Core Idea

Strict separation of concerns:

PostgreSQL → Symbols → JIT Meaning Activation → LLM Reasoning

- SQL stores facts and canonical semantics
- Symbols act as pointers, not meaning containers
- Meaning is computed just-in-time
- The model remains stateless

---

## Design Principles

- No stored meaning
- Meaning is always computed at runtime
- Deterministic storage, probabilistic reasoning
- No hidden long-term cognitive state

---

## What This Repository Is

- An MVP implementation
- Reference tooling and structure
- A safe starting point for experimentation

## What This Repository Is Not

- A vector memory system
- Classical RAG
- Long-term conversational memory
- Agent personality storage

---

## Licensing & Usage

### One Pizza License (OPL)

Use of the **JIT Symbolic Memory Architecture** requires acceptance of the  
**One Pizza License (OPL)**.

**In short:**
- One-time payment
- One (1) pizza per end user
- No recurring fees

After accepting the OPL:
- internal use is fully allowed
- further development and modification are encouraged
- open-source implementations are allowed

Full terms are defined in:

👉 **LICENSING.md**

---

### Publishing Your Own Implementation

If you publish your own implementation (open source or otherwise):

- you must reference the original architecture definition
- you must state that use requires acceptance of the One Pizza License

This keeps the architecture open while preserving clear lineage.

---

### Commercial Use

If the architecture is used as a **core part of a commercial product or service**,  
separate commercial licensing terms must be agreed upon.

Internal use (including within companies) does **not** require a separate agreement.

---

## Payment (OPL)

Current payment method:

- Network: Cronos (EVM)
- Token: any Cronos-supported coin or token
- Address:

0xAddc61aF05ACc594623c3e73D242C17d169A28b2

A confirmed on-chain transaction hash (txid) is sufficient proof.

---

## Summary

- Architecture is defined upstream
- This repository is an MVP
- Pay one pizza → use freely for yourself or internally
- Open-source development is welcome
- Commercial products require a separate agreement

🍕 One Pizza License — simple, fair, and builder-friendly.
