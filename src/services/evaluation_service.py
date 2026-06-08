import json
from pathlib import Path
from typing import Any


def write_metrics(
    metrics: dict[str, Any],
) -> None:

    Path(
        "generated"
    ).mkdir(
        exist_ok=True
    )

    Path(
        "generated/evaluation_metrics.json"
    ).write_text(
        json.dumps(
            metrics,
            indent=2,
        )
    )