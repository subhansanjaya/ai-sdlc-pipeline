ALLOWED_PATHS = [
    "generated/code",
    "generated/tests",
]

def validate_path(
    path: str,
) -> None:

    for allowed in ALLOWED_PATHS:

        if path.startswith(
            allowed
        ):
            return

    raise ValueError(
        f"Unauthorized path: {path}"
    )