# AI SDLC Pipeline

## Overview

AI SDLC Pipeline is a prototype framework that transforms structured feature specifications into implementation artefacts using AI-assisted workflows and automated quality checks.

The project demonstrates how Large Language Models (LLMs), workflow orchestration, human approvals, auditability, observability, and software engineering governance can be combined to support an AI-assisted Software Development Lifecycle (SDLC).

The pipeline supports:

* Feature Specification Intake
* Specification Validation
* Implementation Planning
* AI-Assisted Code Generation
* Automated Test Generation
* Human Approval Workflows
* LangGraph Workflow Orchestration
* SQLite Workflow Checkpointing
* Approve / Reject Workflow Gates
* Prompt Version Management
* Audit Logging
* Evaluation Metrics
* Deployment Evidence Generation
* Observability Dashboard

![screenshot](https://github.com/subhansanjaya/ai-sdlc-pipeline/blob/main/assets/capture1.png)

![screenshot](https://github.com/subhansanjaya/ai-sdlc-pipeline/blob/main/assets/capture4.png)

![screenshot](https://github.com/subhansanjaya/ai-sdlc-pipeline/blob/main/assets/capture2.png)

![screenshot](https://github.com/subhansanjaya/ai-sdlc-pipeline/blob/main/assets/capture3.png)

---

# Quick Start

Clone the repository:

```bash
git clone <repository-url>
cd ai-sdlc-pipeline
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

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

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key

OPENAI_MODEL=gpt-4.1-mini

OLLAMA_MODEL=llama3.1
```

---

# Available CLI Commands

Display available commands:

```bash
python -m src.cli --help
```

Available commands:

```text
version

validate
plan
implement
tests
deploy

approve-implementation
approve-deployment

pipeline
approve
reject

clean
```

---

# LangGraph Workflow Execution

Start the workflow:

```bash
python -m src.cli pipeline specs/order_sorting.md
```

Note: order_sorting.md is a sample specification created for testing purposes.

Expected output:

```text
Workflow paused awaiting approval.
```

Approve and continue execution:

```bash
python -m src.cli approve
```

Reject the workflow:

```bash
python -m src.cli reject
```

Workflow state is persisted to:

```text
workflow.db
```
---

# Manual Pipeline Execution

Validate specification:

```bash
python -m src.cli validate specs/order_sorting.md
```

Generate implementation plan:

```bash
python -m src.cli plan specs/order_sorting.md
```

Approve implementation:

```bash
python -m src.cli approve-implementation subhan
```

Generate implementation:

```bash
python -m src.cli implement specs/order_sorting.md
```

Generate tests:

```bash
python -m src.cli tests specs/order_sorting.md
```

Approve deployment:

```bash
python -m src.cli approve-deployment approverName
```

Generate deployment evidence:

```bash
python -m src.cli deploy
```

---

# Observability Dashboard

Launch the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

Open:

```text
http://localhost:8501
```

The dashboard provides visibility into:

* Audit Logs
* Generated Plans
* Generated Code
* Generated Tests
* Prompt Versions
* Evaluation Metrics
* Deployment Evidence

---

# Generated Artefacts

The pipeline generates artefacts under:

```text
generated/
```

Examples:

```text
generated/plans/
generated/code/
generated/tests/
generated/audit/
generated/approvals/
generated/deployments/
generated/evaluation_metrics.json
generated/traceability.json
```

Workflow checkpoints are stored separately:

```text
workflow.db
```

---

# Development Commands

Run Ruff:

```bash
ruff check src tests
```

Run MyPy:

```bash
mypy src
```

Run Pytest:

```bash
pytest
```

Run all checks before committing changes.

---

# Clean Workspace

Remove generated artefacts and workflow checkpoints:

```bash
python -m src.cli clean
```

This removes:

```text
generated/
workflow.db
```

and recreates a clean workspace.

---

# Architecture

```text
Specification
      ↓
Validation
      ↓
Planning Agent
      ↓
SQLite Checkpoint
      ↓
Approval Gate
      ↓
Approve / Reject
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

# Features

## Specification Intake

Supported formats:

* Markdown (.md)
* YAML (.yaml / .yml)
* JSON (.json)

The pipeline validates specifications before processing.

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

Approval checkpoints exist before:

* Implementation
* Deployment

The LangGraph workflow supports persistent workflow checkpointing using SQLite.

When approval is required, the workflow:

1. Saves workflow state
2. Pauses execution
3. Waits for approval
4. Allows explicit approval or rejection
5. Continues only after approval

---

## LangGraph Workflow Orchestration

Workflow:

```text
Specification
      ↓
Planning
      ↓
Checkpoint
      ↓
Approval Gate
      ↓
Approve / Reject
      ↓
Implementation
      ↓
Test Generation
```

This demonstrates:

* Agent orchestration
* Shared workflow state
* Persistent workflow checkpointing
* Human-in-the-loop approval
* Workflow recovery
* End-to-end SDLC automation

---

## Workflow Persistence

Workflow state is persisted using SQLite.

Benefits:

* Survives application restarts
* Supports long-running approval processes
* Demonstrates production-style workflow orchestration
* Enables workflow recovery

Checkpoint database:

```text
workflow.db
```

---

## Prompt Version Management

Prompts are versioned and loaded centrally.

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

# LangGraph Workflow

## Start Workflow

```bash
python -m src.cli pipeline specs/order_sorting.md
```

Expected output:

```text
Workflow paused awaiting approval.
```

Workflow state is persisted to:

```text
workflow.db
```

---

## Approve Workflow

Continue execution from the saved checkpoint:

```bash
python -m src.cli approve
```

The workflow resumes from the approval checkpoint and continues with:

* Implementation Generation
* Test Generation
* Evaluation Metrics

---

## Reject Workflow

Reject the workflow:

```bash
python -m src.cli reject
```

Expected output:

```text
Workflow rejected.
```

No additional workflow steps are executed.

---

## Clean Workspace

Remove generated artefacts and workflow checkpoints:

```bash
python -m src.cli clean
```

Removes:

```text
generated/
workflow.db
```

---

# Docker Support

Build image:

```bash
docker build -t ai-sdlc-pipeline .
```

Display available commands:

```bash
docker run ai-sdlc-pipeline --help
```

Show version:

```bash
docker run ai-sdlc-pipeline version
```

Run workflow:

```bash
docker run ai-sdlc-pipeline pipeline specs/order_sorting.md
```

Persist generated artefacts and workflow checkpoints:

```bash
docker run \
  -v $(pwd)/generated:/app/generated \
  -v $(pwd)/workflow.db:/app/workflow.db \
  ai-sdlc-pipeline \
  pipeline specs/order_sorting.md
```

This persists:

* Generated artefacts
* Audit logs
* Evaluation metrics
* Workflow checkpoints

allowing workflows to be resumed after container restarts.

Pass environment variables:

```bash
docker run \
  -e OPENAI_API_KEY=<your-api-key> \
  ai-sdlc-pipeline \
  plan specs/order_sorting.md
```

Rebuild image after changes:

```bash
docker build -t ai-sdlc-pipeline .
```

---

# Design Decisions

* Modular architecture
* Provider abstraction for OpenAI and Ollama
* LangGraph workflow orchestration
* SQLite-based workflow checkpointing
* Human approval gates with Approve / Reject actions
* Prompt version management
* File-based audit trail
* Deterministic validation before execution
* Streamlit-based observability dashboard

---

# Trade-Offs

* Simplicity over enterprise-scale orchestration
* SQLite checkpointing instead of distributed workflow storage
* File-based storage instead of database persistence
* Prompt-driven planning rather than strict structured outputs

---

# Limitations

* Generated code quality depends on model capability
* Deployment is simulated through evidence generation
* Limited change impact analysis
* Dashboard uses generated files rather than live telemetry

---

# Future Improvements

* Distributed workflow checkpoint storage (PostgreSQL / Redis)
* Structured LLM outputs using JSON Schema
* GitHub Pull Request automation
* Multi-agent code review
* Persistent audit database
* Policy-as-code governance controls
* Cloud deployment support (AWS, Azure, GCP)
* Workflow visualization and execution history
* Role-based approval workflows
* Multiple concurrent workflow executions

# Usage and Deployment

For more details, see the [Usage and Deployment Guide](https://github.com/subhansanjaya/ai-sdlc-pipeline/blob/main/docs/AI_SDLC_Usage_and_Deployment_Guide.md).
---

# License

This project is licensed under the MIT License. See the LICENSE file for details.
