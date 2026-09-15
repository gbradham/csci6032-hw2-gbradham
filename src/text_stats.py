"""Report basic statistics for a UTF-8 text file."""

import argparse
import json
from pathlib import Path


def text_statistics(path: Path) -> dict[str, int]:
    """Return line, word, and character counts for a UTF-8 text file."""
    text = path.read_text(encoding="utf-8")
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count lines, words, and characters in a UTF-8 text file."
    )
    parser.add_argument("file", type=Path, help="path to the UTF-8 text file")
    args = parser.parse_args()
    print(json.dumps(text_statistics(args.file)))


if __name__ == "__main__":
    main()
