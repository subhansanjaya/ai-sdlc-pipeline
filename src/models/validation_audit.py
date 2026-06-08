from src.services.audit_service import (
    write_audit_record,
)

def audit_validation(
    spec_path: str,
) -> None:

    write_audit_record(
        "validation",
        {
            "spec_path":
                spec_path,
            "status":
                "passed",
        },
    )