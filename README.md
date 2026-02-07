# JIT Symbolic Memory Architecture for LLMs

Stateless semantic memory effect for LLM systems  
PostgreSQL, Symbols, Just-In-Time Meaning, Ollama / LLaMA

---

## TL;DR

Stateless symbolic memory for LLMs:

- store facts and canonical semantics
- compute meaning only at runtime
- keep models honest and repeatable

This architecture produces a memory effect without persistent memory.

One Pizza License applies.

---

## Why this exists

Large Language Models do not have memory in the traditional sense.

Attempts to give them one usually fail by:
- storing interpretations instead of facts
- polluting context windows
- creating hidden state
- mixing probabilistic reasoning with deterministic storage

This architecture takes the opposite approach:

LLMs should not store meaning.  
They should compute it when needed.

---

## Core Idea

Memory effect without memory by strict separation:

PostgreSQL -> Symbols -> JIT Meaning Activation -> LLM Reasoning

- SQL stores facts and canonical semantics
- Symbols are pointers, not meaning containers
- Meaning is computed just-in-time
- LLM remains stateless

---

## Design Principles

- No stored meaning
- Meaning computed at runtime
- Stateless reasoning
- Deterministic storage

---

## License

Attribution-Only, No-Derivatives License (A-ND)

Copyright (c) 2026  
Aki Hirvilammi

---

## One Pizza License (OPL)

- One-time fee
- One pizza per end user
- Pizza price is the average price in the user's country
- No recurring payments

Payment network: Cronos (EVM)

Payment address:

0xAddc61aF05ACc594623c3e73D242C17d169A28b2
