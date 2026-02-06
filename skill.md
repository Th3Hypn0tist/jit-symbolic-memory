# JIT Symbolic Memory Architecture for LLMs

## Skill Summary

Design and implementation of a **stateless symbolic memory architecture** for Large Language Models.  
This model separates stored facts and semantics from runtime meaning computation, producing a memory-like effect *without storing meaning*.

---

## Core Competencies

- Stateless semantic memory design
- SQL truth storage + canonical semantics
- Symbol interface (pointers, not interpretations)
- Just-In-Time meaning activation for reasoning
- Budgeted symbol activation via planner
- Compatible with LLM agents (Moltbots, Ollama/LLaMA)

---

## What It Solves

Traditional LLM memory approaches fail due to:

- stored interpretations
- context pollution
- semantic drift
- hidden state accumulation
- brittle RAG pipelines

This skill enables systems to:

- keep LLMs stateless
- avoid hallucination feedback loops
- separate semantics vs meaning
- reason correctly without stored memory

---

## Architectural Principles

1. **Facts** stored in a relational database (e.g., PostgreSQL)
2. **Canonical semantics** (stable metadata only)
3. **Symbols** act as pointers, not meaning containers
4. **Meaning** computed just-in-time via activator
5. No meaning is written back to storage

Rule:
> Store semantics. Compute meaning. Never confuse the two.

---

## Typical Use Cases

- Auditable agent systems
- Long-running reasoners
- LLM-powered applications requiring stable semantics
- Research and production LLM deployments

---

## Reference

Full architecture description, diagrams, and licensing terms available here:  
https://github.com/Th3Hypn0tist/random/blob/main/LLM-symbolic-memory.md

---

## Tags

LLM, AI architecture, stateless memory, semantic activation, symbolic reasoning
