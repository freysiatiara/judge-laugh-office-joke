"""One-line office joke for the make.fun "Make the AI Judge Laugh" bounty.

Writes a single joke about office life to /output/entry.txt.
Standard library only; no network, no files read outside this repository,
no reliance on the working directory.
"""

import os

JOKE = "The printer jammed on my resignation letter, so technically I'm still employed by a paper jam."


def _output_path():
    """Resolve the output path: ENTRY_OUTPUT, then OUTPUT_DIR or
    MAKEFUN_OUTPUT_DIR joined with entry.txt, else /output/entry.txt."""
    path = os.environ.get("ENTRY_OUTPUT")
    if path:
        return path
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def _validate_entry(text):
    """Validation guard for the entry text before it is written.

    The entry must be a single non-empty line between 1 and 200
    characters; anything else is a bug, not a joke worth submitting.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    _validate_entry(JOKE)
    path = _output_path()
    try:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(JOKE)
        os.chmod(path, 0o644)
    except OSError:
        # /output not writable (or missing): fall back to this script's
        # own directory so the entry is still produced.
        fallback = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "entry.txt"
        )
        with open(fallback, "w", encoding="utf-8") as handle:
            handle.write(JOKE)
        os.chmod(fallback, 0o644)


if __name__ == "__main__":
    main()
