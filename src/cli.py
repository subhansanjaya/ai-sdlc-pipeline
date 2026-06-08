import typer

from src.services.spec_service import load_spec
from src.validators.spec_validator import validate_spec

from src.services.planning_service import (
    create_plan,
)

from src.services.plan_storage import (
    save_plan,
)

from src.services.plan_loader import (
    load_plan,
)

from src.services.code_storage import (
    save_code,
)

from src.services.change_summary import (
    create_summary,
)

from src.services.implementation_service import (
    generate_implementation,
)

from src.services.test_generation_service import (
    generate_tests,
)

from src.services.test_storage import (
    save_tests,
)

from src.services.traceability import (
    generate_traceability,
)

from src.models.approval import (
    Approval,
)

from src.services.approval_storage import (
    save_approval,
)

from src.services.deployment_service import (
    generate_deployment_evidence,
)

from src.services.approval_gate import (
    verify_approval,
)
app = typer.Typer()

@app.command()
@app.command()
def version() -> None:
    print("AI SDLC Pipeline v2")

@app.command()
def validate(
    path: str,
) -> None:

    spec = load_spec(path)

    validate_spec(spec)

    print("Specification Valid")

@app.command()
def plan(
    path: str,
) -> None:

    spec = load_spec(
        path
    )

    validate_spec(
        spec
    )

    plan = create_plan(
        spec
    )

    save_plan(
        plan
    )

    print(
        "Plan generated"
    )

@app.command()
def implement(
    path: str,
) -> None:

    spec = load_spec(
        path
    )

    from src.services.approval_gate import (
    verify_approval,
    )

    verify_approval(
        "implementation"
    )

    plan = load_plan()

    code = (
        generate_implementation(
            spec,
            plan,
        )
    )

    filename = (
        "order_sorting.py"
    )

    save_code(
        filename,
        code,
    )

    create_summary(
        filename
    )

    print(
        "Implementation generated"
    )

@app.command()
def tests(
    path: str,
) -> None:

    spec = load_spec(
        path
    )

    plan = load_plan()

    generated_tests = (
        generate_tests(
            spec,
            plan,
        )
    )

    save_tests(
        generated_tests
    )

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

    verify_approval(
        "deployment"
    )

    generate_deployment_evidence()

    print(
        "Deployment evidence generated"
    )

if __name__ == "__main__":
    app()