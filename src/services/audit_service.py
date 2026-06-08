import json
from pathlib import Path
from datetime import datetime
from typing import Any

def write_audit_record(
    event_type: str,
    payload: dict[str, Any],
) -> None:

    Path(
        "generated/audit"
    ).mkdir(
        parents=True,
        exist_ok=True,
    )

    file_path = (
        Path(
            "generated/audit/audit_log.jsonl"
        )
    )

    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "payload": payload,
    }

    with open(
        file_path,
        "a",
    ) as file:
        file.write(
            json.dumps(record)
        )
        file.write("\n")