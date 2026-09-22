import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROGRAM = PROJECT_ROOT / "src" / "text_stats.py"


class TextStatsTests(unittest.TestCase):
    def run_program(self, content: str, *args: str) -> dict[str, object]:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", suffix=".txt", delete=False
        ) as text_file:
            text_file.write(content)
            path = Path(text_file.name)
        try:
            result = subprocess.run(
                [sys.executable, str(PROGRAM), str(path), *args],
                check=True,
                capture_output=True,
                text=True,
            )
        finally:
            path.unlink()
        return json.loads(result.stdout)

    def test_counts_lines_words_and_unicode_characters(self) -> None:
        self.assertEqual(
            self.run_program("Café au lait\n第二行\n"),
            {"lines": 2, "words": 4, "characters": 17},
        )

    def test_empty_file_has_zero_counts(self) -> None:
        self.assertEqual(
            self.run_program(""),
            {"lines": 0, "words": 0, "characters": 0},
        )

    def test_top_words_are_case_insensitive_and_ties_are_alphabetical(self) -> None:
        self.assertEqual(
            self.run_program("Beta alpha ALPHA beta gamma", "--top", "3"),
            {
                "lines": 1,
                "words": 5,
                "characters": 27,
                "top": [
                    {"word": "alpha", "count": 2},
                    {"word": "beta", "count": 2},
                    {"word": "gamma", "count": 1},
                ],
            },
        )

    def test_top_zero_returns_no_words(self) -> None:
        self.assertEqual(
            self.run_program("one two", "--top", "0")["top"],
            [],
        )


if __name__ == "__main__":
    unittest.main()
