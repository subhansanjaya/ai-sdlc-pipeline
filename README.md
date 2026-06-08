# AI SDLC Pipeline

## Overview

AI SDLC Pipeline is a prototype framework that transforms a structured feature specification into implementation artefacts using AI-assisted workflows and deterministic quality controls.

The pipeline supports:

* Feature Specification Intake
* Specification Validation
* Implementation Planning
* AI-Assisted Code Generation
* Automated Test Generation
* Human Approval Workflows
* Audit Logging
* Deployment Evidence Generation

The goal is to demonstrate traceability, governance, and reproducibility across an AI-assisted software delivery lifecycle.

---

# Architecture

```text
Specification
      ↓
Validation
      ↓
Planning Layer
      ↓
Implementation Approval
      ↓
AI-Assisted Implementation
      ↓
Test Generation
      ↓
Deployment Approval
      ↓
Deployment Evidence
      ↓
Audit Trail
```

---

# Features

## Specification Intake

Supported formats:

* Markdown (.md)
* YAML (.yaml / .yml)
* JSON (.json)

The pipeline validates that required sections exist before processing.

## Planning Layer

Generates:

* Implementation Tasks
* Technical Design Summary
* Impacted Modules
* Risks
* Test Strategy

## AI-Assisted Implementation

Generates source code from:

* Approved Feature Specification
* Approved Implementation Plan

Supported providers:

* OpenAI
* Ollama

## Automated Test Generation

Generates:

* Unit Tests
* Integration Tests
* Acceptance Tests

## Human Approval Workflow

Approval checkpoints before:

* Implementation
* Deployment

## Auditability

Captures:

* Generated Plans
* Approvals
* Generated Outputs
* Validation Results
* Deployment Evidence

---

# Project Structure

```text
ai-sdlc-pipeline/

├── .github/
│   └── workflows/
│       └── ci.yml
│
├── specs/
│
├── src/
│   ├── agents/
│   ├── models/
│   ├── parser/
│   ├── providers/
│   ├── services/
│   └── validators/
│
├── tests/
│
├── generated/
│   ├── plans/
│   ├── code/
│   ├── tests/
│   ├── approvals/
│   ├── audit/
│   └── deployment/
│
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# Prerequisites

* Python 3.12
* Git

Recommended:

* VS Code

---

# Installation

Clone repository:

```bash
git clone <repository-url>
cd ai-sdlc-pipeline
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key

OPENAI_MODEL=gpt-4.1-mini

OLLAMA_MODEL=llama3.1
```

Provider configuration:

```yaml
provider: openai
```

or

```yaml
provider: ollama
```

---

# Running the Pipeline

## Validate Specification

Note: I have added a simple specification to test the functionality order_sorting.md

```bash
python -m src.cli validate specs/order_sorting.md
```

---

## Generate Implementation Plan

```bash
python -m src.cli plan specs/order_sorting.md
```

Output:

```text
generated/plans/plan.json
```

---

## Approve Implementation

```bash
python -m src.cli approve-implementation nameOfTheApprover
```

Output:

```text
generated/approvals/implementation.json
```

---

## Generate Implementation

```bash
python -m src.cli implement specs/order_sorting.md
```

Output:

```text
generated/code/
```

---

## Generate Tests

```bash
python -m src.cli tests specs/order_sorting.md
```

Output:

```text
generated/tests/
generated/traceability.json
```

---

## Approve Deployment

```bash
python -m src.cli approve-deployment nameOfTheApprover
```

---

## Generate Deployment Evidence

```bash
python -m src.cli deploy
```

Output:

```text
generated/deployment/deployment_evidence.json
```

---

# Quality Gates

Run linting:

```bash
ruff check src tests
```

Run type checking:

```bash
mypy src
```

Run tests:

```bash
pytest
```

---

# GitHub Actions

CI pipeline executes:

* Ruff
* MyPy
* Pytest



Workflow file:

```text
.github/workflows/ci.yml
```

---

# Example End-to-End Execution

```bash
python -m src.cli validate specs/order_sorting.md

python -m src.cli plan specs/order_sorting.md

python -m src.cli approve-implementation subhan

python -m src.cli implement specs/order_sorting.md

python -m src.cli tests specs/order_sorting.md

python -m src.cli approve-deployment subhan

python -m src.cli deploy
```

---

# Design Decisions

* Modular architecture
* Provider abstraction for OpenAI and Ollama
* Human approval checkpoints
* File-based audit trail
* Deterministic validation before execution

---

# Trade-Offs

* Simplicity over enterprise-scale orchestration
* File-based storage instead of database persistence
* Prompt-driven planning rather than strict structured outputs

---

# Limitations

* Generated code quality depends on model capability
* Approval workflow is file-based
* Deployment is simulated through evidence generation
* Limited change impact analysis

---

# Future Improvements

* LangGraph workflow orchestration
* Structured LLM outputs using JSON Schema
* GitHub Pull Request automation
* Multi-agent code review
* Containerized execution
* Persistent audit database
* Policy-as-code governance controls

---

# usage and Deployment

Please refer to [Link Text](docs/AI_SDLC_Usage_and_Deployment_Guide.md) 

## License

This project is licensed under the MIT License. See the LICENSE file for details.