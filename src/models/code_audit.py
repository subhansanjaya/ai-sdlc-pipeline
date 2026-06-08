from src.services.audit_service import (
    write_audit_record,
)

def audit_generated_code(
    filename: str,
) -> None:

    write_audit_record(
        "code_generated",
        {
            "file":
                filename,
        },
    )