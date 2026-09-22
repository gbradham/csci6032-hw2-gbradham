"""Report basic statistics for a UTF-8 text file."""

import argparse
from collections import Counter
import json
from pathlib import Path


def text_statistics(path: Path, top: int | None = None) -> dict[str, object]:
    """Return line, word, and character counts for a UTF-8 text file."""
    text = path.read_text(encoding="utf-8")
    statistics: dict[str, object] = {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }
    if top is not None:
        counts = Counter(word.casefold() for word in text.split())
        statistics["top"] = [
            {"word": word, "count": count}
            for word, count in sorted(
                counts.items(), key=lambda item: (-item[1], item[0])
            )[:top]
        ]
    return statistics


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count lines, words, and characters in a UTF-8 text file."
    )
    parser.add_argument("file", type=Path, help="path to the UTF-8 text file")
    parser.add_argument(
        "--top",
        type=int,
        metavar="N",
        help="include the N most frequent words, case-insensitively",
    )
    args = parser.parse_args()
    if args.top is not None and args.top < 0:
        parser.error("--top must be non-negative")
    print(json.dumps(text_statistics(args.file, args.top)))


if __name__ == "__main__":
    main()
