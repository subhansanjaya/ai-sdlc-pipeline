"""
CLI entry point for the AI SDLC Pipeline.

Supports both:
- Manual stage-by-stage execution
- End-to-end LangGraph workflow execution

This file orchestrates specification validation,
planning, implementation, testing, approvals,
deployment evidence generation, and cleanup.
"""

import shutil
from pathlib import Path

import typer

# Specification loading and validation
from src.services.spec_service import load_spec
from src.validators.spec_validator import validate_spec

# Planning services
from src.services.planning_service import create_plan
from src.services.plan_storage import save_plan
from src.services.plan_loader import load_plan

# Implementation services
from src.services.implementation_service import generate_implementation
from src.services.code_storage import save_code
from src.services.change_summary import create_summary

# Test generation services
from src.services.test_generation_service import generate_tests
from src.services.test_storage import save_tests
from src.services.traceability import generate_traceability

# Approval and deployment services
from src.models.approval import Approval
from src.services.approval_storage import save_approval
from src.services.approval_gate import verify_approval
from src.services.deployment_service import (
    generate_deployment_evidence,
)

# LangGraph workflow
from src.workflow.graph import workflow

from langgraph.types import (
    Command,
)



# Main CLI application.
# Each command represents a stage in the SDLC pipeline.
app = typer.Typer()


@app.command()
def version() -> None:
    """
    Display application version.
    """
    print("AI SDLC Pipeline v2")


@app.command()
def validate(
    path: str,
) -> None:
    """
    Validate a specification file before processing.
    """

    spec = load_spec(path)

    validate_spec(spec)

    print("Specification Valid")


@app.command()
def plan(
    path: str,
) -> None:
    """
    Generate an implementation plan from a specification.
    """

    spec = load_spec(path)

    validate_spec(spec)

    # Generate implementation plan using the Planner Agent.
    plan = create_plan(spec)

    # Persist the plan for downstream stages.
    save_plan(plan)

    print("Plan generated")


@app.command()
def implement(
    path: str,
) -> None:
    """
    Generate implementation code from an approved plan.
    """

    spec = load_spec(path)

    # Ensure implementation approval exists.
    verify_approval(
        "implementation"
    )

    # Load previously generated implementation plan.
    plan = load_plan()

    # Generate implementation code from the
    # specification and implementation plan.
    code = generate_implementation(
        spec,
        plan,
    )

    save_code(
        "order_sorting.py",
        code,
    )

    # Create a summary of generated changes.
    create_summary(
        "order_sorting.py"
    )

    print(
        "Implementation generated"
    )


@app.command()
def tests(
    path: str,
) -> None:
    """
    Generate tests and traceability information.
    """

    spec = load_spec(path)

    # Load implementation plan for test context.
    plan = load_plan()

    # Generate AI-assisted tests.
    generated_tests = generate_tests(
        spec,
        plan,
    )

    save_tests(
        generated_tests
    )

    # Map acceptance criteria to generated tests.
    generate_traceability(
        spec
    )

    print(
        "Tests generated"
    )


@app.command()
def approve_implementation(
    approved_by: str,
) -> None:
    """
    Record implementation approval.
    """

    approval = Approval(
        stage="implementation",
        approved=True,
        approved_by=approved_by,
        comments="Implementation approved",
    )

    save_approval(
        approval
    )

    print(
        "Implementation approved"
    )


@app.command()
def approve_deployment(
    approved_by: str,
) -> None:
    """
    Record deployment approval.
    """

    approval = Approval(
        stage="deployment",
        approved=True,
        approved_by=approved_by,
        comments="Deployment approved",
    )

    save_approval(
        approval
    )

    print(
        "Deployment approved"
    )


@app.command()
def deploy() -> None:
    """
    Generate deployment evidence after approval.
    """

    # Deployment requires explicit approval.
    verify_approval(
        "deployment"
    )

    # Generate deployment evidence for
    # audit and compliance purposes.
    generate_deployment_evidence()

    print(
        "Deployment evidence generated"
    )


@app.command()
def pipeline(
    path: str,
) -> None:
    """
    Execute the complete SDLC workflow using LangGraph.

    Flow:

    Specification
        ↓
    Validation
        ↓
    Planning
        ↓
    Human Approval
        ↓
    Implementation
        ↓
    Test Generation
        ↓
    Complete

    Demonstrates agent orchestration and
    human-in-the-loop approval using LangGraph.
    """

    # Load specification and initialize workflow state.
    spec = load_spec(path)

    # Execute the LangGraph workflow.
    config = {
        "configurable": {
            "thread_id":
                "order_sorting"
        }
    }

    result = workflow.invoke(
        {
            "spec": spec,
            "plan": None,
            "code": None,
            "tests": None,
        },
        config=config,
    )
    if "__interrupt__" in result:

        print(
            "Workflow paused awaiting approval."
        )

        return

# To demonstrate manual resumption of the workflow after approval,
# we can implement a resume command. In a real application, this would likely be triggered by an event or callback after the human approval step is completed.
# @app.command()
# def resume() -> None:
#     """
#     Resume a paused workflow.
#     """

#     result = workflow.invoke(
#         Command(
#             resume=True
#         ),
#         config={
#             "configurable": {
#                 "thread_id":
#                     "order_sorting"
#             }
#         }
#     )

#     print(result)


@app.command()
def approve() -> None:
    """
    Approve a paused workflow and continue execution.
    """

    workflow.invoke(
        Command(
            resume="approve"
        ),
        config={
            "configurable": {
                "thread_id":
                    "order_sorting"
            }
        }
    )

    print(
        "Workflow approved and completed."
    )

@app.command()
def reject() -> None:
    """
    Reject a paused workflow.
    """

    try:

        workflow.invoke(
            Command(
                resume="reject"
            ),
            config={
                "configurable": {
                    "thread_id":
                        "order_sorting"
                }
            }
        )

    except ValueError:

        print(
            "Workflow rejected."
        )

@app.command()
def clean() -> None:
    """
    Remove all generated artifacts.

    Useful during development and demos to
    reset the workspace and start fresh.
    """

    db_file = Path(
    "workflow.db"
    )

    if db_file.exists():
        db_file.unlink()

    generated = Path(
        "generated"
    )

    if generated.exists():

        shutil.rmtree(
            generated
        )

    generated.mkdir(
        exist_ok=True
    )

    print(
        "Generated artifacts removed"
    )

if __name__ == "__main__":
    app()