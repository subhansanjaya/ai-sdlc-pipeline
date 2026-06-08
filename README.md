# AI SDLC Pipeline

## Overview

AI SDLC Pipeline is a prototype framework that transforms structured feature specifications into implementation artefacts using AI-assisted workflows and deterministic quality controls.

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

---

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

---

# Usage and Deployment

Refer to:

```text
docs/AI_SDLC_Usage_and_Deployment_Guide.md
```

---

# License

This project is licensed under the MIT License. See the LICENSE file for details.
