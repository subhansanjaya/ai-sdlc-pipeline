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


# Main CLI application
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

    plan = create_plan(spec)

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

    # Ensure implementation approval exists
    verify_approval(
        "implementation"
    )

    plan = load_plan()

    code = generate_implementation(
        spec,
        plan,
    )

    save_code(
        "order_sorting.py",
        code,
    )

    # Create a simple summary of generated changes
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

    plan = load_plan()

    generated_tests = generate_tests(
        spec,
        plan,
    )

    save_tests(
        generated_tests
    )

    # Map acceptance criteria to generated tests
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

    verify_approval(
        "deployment"
    )

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
    Planning
        ↓
    Human Approval
        ↓
    Implementation
        ↓
    Test Generation
    """

    spec = load_spec(
        path
    )

    result = workflow.invoke(
        {
            "spec": spec,
            "plan": None,
            "code": None,
            "tests": None,
        }
    )

    print(result)


if __name__ == "__main__":
    app()