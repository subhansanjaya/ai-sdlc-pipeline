import json
from datetime import datetime
from pathlib import Path

def generate_deployment_evidence() -> None:

    Path(
        "generated/deployment"
    ).mkdir(
        parents=True,
        exist_ok=True,
    )

    evidence = {
        "deployment_time":
            datetime.utcnow().isoformat(),
        "status":
            "approved",
    }

    Path(
        "generated/deployment/deployment_evidence.json"
    ).write_text(
        json.dumps(
            evidence,
            indent=2,
        )
    )