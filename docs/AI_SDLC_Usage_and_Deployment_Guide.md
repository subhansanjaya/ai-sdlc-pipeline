# AI SDLC Pipeline - Usage, Deployment and Future Roadmap

## How Someone Uses This Project

### Current Prototype Workflow

Product Manager / Business Analyst
→ Creates Feature Specification
→ Developer runs CLI commands
→ AI generates implementation plan
→ Human approval
→ AI generates code
→ AI generates tests
→ Quality gates run
→ Human deployment approval
→ Deployment evidence generated

## Example End-to-End Usage

python -m src.cli validate specs/order_sorting.md
python -m src.cli plan specs/order_sorting.md
python -m src.cli approve-implementation subhan
python -m src.cli implement specs/order_sorting.md
python -m src.cli tests specs/order_sorting.md
python -m src.cli approve-deployment subhan
python -m src.cli deploy

## Who Uses It

- Product Owner / Business Analyst
- AI Planner
- Tech Lead
- AI Implementation Agent
- AI Test Agent
- Release Manager
- Auditor

## Current Deployment Model

The prototype does not perform a real cloud deployment.
It generates deployment evidence demonstrating governance and approval workflows.

## Production Version Options

1. GitHub-centric workflow
2. Web application (React + FastAPI)
3. Jira integration

## AWS Deployment Architecture

GitHub
→ GitHub Actions
→ Docker Build
→ Amazon ECR
→ Amazon ECS/EKS
→ Production

## Future Improvements

- LangGraph orchestration
- Structured LLM outputs
- GitHub PR automation
- AWS ECS deployment
- Kubernetes deployment
- FastAPI backend
- React frontend
- Jira integration
- Persistent audit database

## Summary

This project demonstrates an AI-assisted SDLC pipeline that converts structured feature specifications into implementation plans, generated code, automated tests, approval records, audit logs, and deployment evidence while enforcing governance and quality controls.
