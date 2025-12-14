from pathlib import Path


class InputError(Exception):
    """Raised when input text cannot be loaded."""
    pass


def load_text_file(path: str) -> str:
    file_path = Path(path)

    if not file_path.exists():
        raise InputError(f"Input text file does not exist: {path}")

    try:
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raise InputError(
            f"Input file is not valid UTF-8 text: {path}"
        )
