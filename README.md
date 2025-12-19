# A.U.R.A. Core Prototype
**Artificial Ubiquitous Reality Analysis – Core Engine (Prototype)**

This repository contains the **first working prototype** of the A.U.R.A. framework.

A.U.R.A. is a research-oriented system designed to analyze **stream of consciousness** narratives and other non-linear texts, in order to study how Large Language Models (LLMs) infer meaning, structure, and “reality” from fragmented input.

This prototype focuses on delivering a **minimal end-to-end pipeline**:
- A Python CLI (`aura`)  
- YAML-based experiment configuration  
- Pluggable LLM providers (OpenAI + mock)  
- A minimal analytical pipeline:
  - Surface analysis
  - Semantic analysis
  - Inference / world-model reconstruction
- Structured JSON outputs
- Token-budget awareness (basic)

---

## Usage

See [AURA CORE PROTOTYPE v0.1](https://github.com/emiliano-poggi/aura-core-prototype/wiki/AURA-CORE-PROTOTYPE-v0.1)

---

## Releases

### v0.1 - Initial prototype release of Artificial Ubiquitous Reality Analysis (A.U.R.A.)  

Features:
- Installable CLI-based prototype (aura)
- YAML-driven experiment configuration
- Narrative text loading from external files
- Deterministic surface analysis
- Semantic and inference analysis via a cognitive engine abstraction
- Mock cognitive engine (default)
- Optional OpenAI-backed cognitive engine via environment variable
- Automatic fallback to mock engine when no API key is present

See also:
- [milestone 0.1.*](https://github.com/emiliano-poggi/aura-core-prototype/milestone/1?closed=1) for the list of closed stories.
- [Wiki AURA CORE PROTOTYPE v0.1](https://github.com/emiliano-poggi/aura-core-prototype/wiki/AURA-CORE-PROTOTYPE-v0.1)] for usage.

---

## Roadmap

### v0.2 - Local LLM provider support

- The next version will focus on local LLM provider support, enabling fully offline and zero-cost cognitive analysis.
- See [milestone 0.2.*](https://github.com/emiliano-poggi/aura-core-prototype/milestone/2) for the list of related stories. 

---

## AURA Repository Model

- `src/aura/`: Core sources
- `src/aura/llm`: Congnitive engine providers
- `src/aura/pipeline`: The analytical pipeline
- `src/aura/utils`: General utilities
- `src/aura/runner.py`: The runner of the experiments
- `src/aura/config.py`: Configuration
- `src/aura/cli.py`: Click cli interface
- `experiments/`: Example experiments and texts
