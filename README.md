# A.U.R.A. Core Prototype
**Artificial Ubiquitous Reality Analysis – Core Engine (Prototype)**

This repository contains the **first working prototype** of the A.U.R.A. framework.

A.U.R.A. is a research-oriented system designed to analyze **stream of consciousness** narratives and other non-linear texts, in order to study how Large Language Models (LLMs) infer meaning, structure, and “reality” from fragmented input.

This prototype focuses on delivering a **minimal end-to-end pipeline**:
- narrative input
- configurable experiment
- LLM-driven analysis
- structured, reproducible outputs

---

## Scope of the Prototype

This prototype implements:

- A Python CLI (`aura`)  
- YAML-based experiment configuration  
- Pluggable LLM providers (OpenAI + mock)  
- A minimal analytical pipeline:
  - Surface analysis
  - Semantic analysis
  - Inference / world-model reconstruction
- Structured JSON outputs
- Token-budget awareness (basic)

This is **not** the final architecture.  
It is a research MVP meant to validate methodology and workflow.

---

## Repository Structure

```text
src/aura/        Core package
experiments/    Example experiments and texts
outputs/        Generated results (ignored by git)
