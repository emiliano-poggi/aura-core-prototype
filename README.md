# A.U.R.A. Core Prototype
**Artificial Ubiquitous Reality Analysis – Core Engine (Prototype)**

This repository contains the **first working prototype** of the A.U.R.A. framework.

A.U.R.A. is a research-oriented system designed to analyze through AI complex language structures based on **stream of consciousness** narratives and other non-linear texts, in order to study how Large Language Models (LLMs) infer meaning, structure, and “reality” from fragmented input.

This prototype focuses on delivering a **minimal end-to-end pipeline**:
- A Python CLI (`aura`)  
- YAML-based experiment configuration  
- Pluggable LLM providers (Mock, OpenAI, local provider like Ollama)  
- A minimal analytical pipeline:
  - Surface analysis
  - Semantic analysis
  - Inference / world-model reconstruction
- Unparsed AI console responses
- Structured (parsed by AURA) JSON console responses
- Prioritizes **clarity and research integrity** over performance or productization

⚠️ **Important**
This repository is intentionally **frozen at v0.2** and serves as a **reference implementation**.
Active development continues in a separate repository (see `aura-core`).

---

## Behavior and Usage

See [AURA CORE PROTOTYPE v0.2](https://github.com/emiliano-poggi/aura-core-prototype/wiki/AURA-CORE-PROTOTYPE-v0.2)

---

## Releases

- [0.2](https://github.com/emiliano-poggi/aura-core-prototype/milestone/2?closed=2)
- [0.1](https://github.com/emiliano-poggi/aura-core-prototype/milestone/1?closed=1)

---

## Roadmap

- Prototype complete at **v0.2**
- No further features planned in this repository
- Code preserved for reference, comparison, and documentation

Future development continues in **`aura-core`**, which reimplements validated concepts in a clean, long-term codebase.
