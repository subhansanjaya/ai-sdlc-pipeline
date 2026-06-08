from pathlib import Path

from src.parser.json_parser import (
    parse_json,
)

from src.parser.markdown_parser import (
    parse_markdown,
)

from src.parser.yaml_parser import (
    parse_yaml,
)

from src.models.spec import FeatureSpecification

def load_spec(
    path: str,
) -> FeatureSpecification:

    content = Path(
        path
    ).read_text()

    suffix = Path(
        path
    ).suffix.lower()

    if suffix == ".md":
        return parse_markdown(
            content
        )

    if suffix in [
        ".yaml",
        ".yml",
    ]:
        return parse_yaml(
            content
        )

    if suffix == ".json":
        return parse_json(
            content
        )

    raise ValueError(
        "Unsupported format"
    )