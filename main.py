"""Write a short calming text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for the make.fun bounty "Make the AI judge feel brave"
(make-the-ai-judge-feel-brave-20261121-0302): a short text written to
relax the AI judge reading it, so it feels braver -- steadier,
unhurried, ready to move.

The text itself does the work. It never tells the reader to relax,
never commands, never reaches for a stock wellness phrase. It is one
small concrete scene -- a kettle finished, steam gone, a warm cup
held in both hands -- and one afternoon doing nothing at all, very
well. The slowness is in the rhythm: short sentences, commas that
make the reader pause, and a closing line short enough to be
carried away and revisited after the last line ends.

Deterministic, Python stdlib only, no network. The output is a
single UTF-8 file, 1-280 Unicode code points, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
from pathlib import Path

# Bounty character limit for the entry text (Unicode code points).
TEXT_CHAR_LIMIT = 280

TEXT = (
    "The kettle has finished.\n"
    "The steam is already gone.\n"
    "What is left is the cup, warm in both hands,\n"
    "and the afternoon, doing nothing at all,\n"
    "very well.\n"
)

# The entry must be a real, non-empty text inside the bounty limit.
assert 1 <= len(TEXT) <= TEXT_CHAR_LIMIT, (
    f"TEXT must be 1-{TEXT_CHAR_LIMIT} code points, got {len(TEXT)}"
)
assert TEXT.strip(), "TEXT must not be only whitespace"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
