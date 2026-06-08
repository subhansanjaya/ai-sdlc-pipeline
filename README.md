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
* LangGraph Workflow Orchestration
* Prompt Version Management
* Audit Logging
* Evaluation Metrics
* Deployment Evidence Generation
* Observability Dashboard

The goal is to demonstrate traceability, governance, reproducibility, and human oversight across an AI-assisted software delivery lifecycle.

---

# Architecture

```text
Specification
      ↓
Validation
      ↓
Planning Agent
      ↓
Human Approval
      ↓
Implementation Agent
      ↓
Test Generation Agent
      ↓
Evaluation Metrics
      ↓
Deployment Approval
      ↓
Deployment Evidence
      ↓
Audit Trail
      ↓
Observability Dashboard
```

---

# Features

## Specification Intake

Supported formats:

* Markdown (.md)
* YAML (.yaml / .yml)
* JSON (.json)

The pipeline validates that required sections exist before processing.

---

## Planning Layer

Generates:

* Implementation Tasks
* Technical Design Summary
* Impacted Modules
* Risks
* Test Strategy

---

## AI-Assisted Implementation

Generates source code from:

* Approved Feature Specification
* Approved Implementation Plan

Supported providers:

* OpenAI
* Ollama

---

## Automated Test Generation

Generates:

* Unit Tests
* Integration Tests
* Acceptance Tests

---

## Human Approval Workflow

Approval checkpoints before:

* Implementation
* Deployment

Additionally, the project includes a LangGraph-based workflow with a human approval node that pauses execution before implementation.

---

## LangGraph Workflow Orchestration

The project includes a LangGraph workflow that orchestrates the software delivery lifecycle.

Workflow:

```text
Specification
      ↓
Planning
      ↓
Human Approval
      ↓
Implementation
      ↓
Test Generation
```

This demonstrates:

* Agent orchestration
* Shared workflow state
* Human-in-the-loop approval
* End-to-end SDLC automation

---

## Prompt Version Management

Prompts are versioned and loaded through a centralized configuration mechanism.

Benefits:

* Prompt traceability
* Easier experimentation
* Reproducible AI outputs
* Auditability

Example:

```yaml
planner_prompt_version: planner_v1
implementation_prompt_version: implementation_v1
test_prompt_version: tests_v1
```

---

## Evaluation Metrics

The pipeline generates evaluation metrics for AI-generated outputs.

Metrics include:

* Prompt Version
* Test Length
* Acceptance Criteria Count

Output:

```text
generated/evaluation_metrics.json
```

---

## Auditability

Captures:

* Generated Plans
* Approvals
* Generated Outputs
* Validation Results
* Deployment Evidence
* Prompt Versions

---

## Observability Dashboard

A Streamlit dashboard provides visibility into:

* Audit Events
* Generated Plans
* Implementations
* Tests
* Prompt Versions
* Evaluation Metrics
* Deployment Activity

---

# Project Structure

```text
ai-sdlc-pipeline/

├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docs/
│
├── specs/
│
├── src/
│   ├── agents/
│   ├── models/
│   ├── parser/
│   ├── prompts/
│   ├── providers/
│   ├── services/
│   ├── validators/
│   └── workflow/
│       ├── state.py
│       ├── nodes.py
│       └── graph.py
│
├── tests/
│
├── generated/
│   ├── plans/
│   ├── code/
│   ├── tests/
│   ├── approvals/
│   ├── audit/
│   ├── deployments/
│   └── evaluation_metrics.json
│
├── dashboard.py
├── requirements.txt
├── pyproject.toml
├── Dockerfile
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

Prompt configuration:

```yaml
planner_prompt_version: planner_v1
implementation_prompt_version: implementation_v1
test_prompt_version: tests_v1
```

---

# Running the Pipeline

## Validate Specification

A sample specification is included:

```text
specs/order_sorting.md
```

Validate the specification:

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
python -m src.cli approve-implementation subhan
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
generated/evaluation_metrics.json
```

---

## Approve Deployment

```bash
python -m src.cli approve-deployment subhan
```

---

## Generate Deployment Evidence

```bash
python -m src.cli deploy
```

Output:

```text
generated/deployments/deployment_evidence.json
```

---

## Run End-to-End LangGraph Workflow

Execute the complete workflow using LangGraph:

```bash
python -m src.cli pipeline specs/order_sorting.md
```

Workflow:

```text
Specification
      ↓
Planning
      ↓
Human Approval
      ↓
Implementation
      ↓
Test Generation
```

When prompted:

```text
Approve implementation? (y/n):
```

Enter:

```text
y
```

to continue execution.

---

## Clean Generated Artifacts

Remove all generated files and start with a clean workspace:

```bash
python -m src.cli clean
```

This removes all generated artifacts and recreates an empty generated directory.

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
* CLI Smoke Test
* Pytest

Workflow file:

```text
.github/workflows/ci.yml
```

The CLI smoke test verifies that the application starts successfully and all imports resolve correctly.

---

# Observability Dashboard

Install dashboard dependencies:

```bash
pip install streamlit pandas
```

Launch dashboard:

```bash
streamlit run dashboard.py
```

The dashboard displays:

* Audit Logs
* Evaluation Metrics
* Generated Plans
* Generated Tests
* Prompt Versions
* Deployment Activity

Dashboard data is sourced from:

```text
generated/audit/
generated/evaluation_metrics.json
generated/approvals/
generated/deployments/
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

Or execute the LangGraph workflow:

```bash
python -m src.cli pipeline specs/order_sorting.md
```

---

# Docker Support

The project can also be executed inside a Docker container without requiring a local Python installation.

## Build Image

```bash
docker build -t ai-sdlc-pipeline .
```

## Display Available Commands

```bash
docker run ai-sdlc-pipeline --help
```

## Show Version

```bash
docker run ai-sdlc-pipeline version
```

## Run LangGraph Workflow

```bash
docker run ai-sdlc-pipeline pipeline specs/order_sorting.md
```

## Persist Generated Artifacts

```bash
docker run \
  -v $(pwd)/generated:/app/generated \
  ai-sdlc-pipeline \
  pipeline specs/order_sorting.md
```

This maps the local generated directory to the container so generated plans, code, tests, approvals, audit logs, metrics, and deployment evidence remain available outside the container.

## Environment Variables

```bash
docker run \
  -e OPENAI_API_KEY=<your-api-key> \
  ai-sdlc-pipeline \
  plan specs/order_sorting.md
```

## Rebuild After Changes

```bash
docker build -t ai-sdlc-pipeline .
```

---

# Design Decisions

* Modular architecture
* Provider abstraction for OpenAI and Ollama
* LangGraph workflow orchestration
* Human approval checkpoints
* Prompt version management
* File-based audit trail
* Deterministic validation before execution

---

# Trade-Offs

* Simplicity over enterprise-scale orchestration
* File-based storage instead of database persistence
* Prompt-driven planning rather than strict structured outputs
* Human approvals are currently CLI-based

---

# Limitations

* Generated code quality depends on model capability
* Approval workflow is file-based
* Deployment is simulated through evidence generation
* Limited change impact analysis
* Dashboard uses generated files rather than live telemetry

---

# Future Improvements

* Advanced LangGraph checkpoint/resume workflows
* Structured LLM outputs using JSON Schema
* GitHub Pull Request automation
* Multi-agent code review
* Persistent audit database
* Policy-as-code governance controls
* Cloud deployment support (AWS, Azure, GCP)

---

# Usage and Deployment

Please refer to:

```text
docs/AI_SDLC_Usage_and_Deployment_Guide.md
```

---

# License

This project is licensed under the MIT License. See the LICENSE file for details.
