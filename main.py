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


def main():
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
