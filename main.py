"""One sentence for a traveler from 1800.

Writes one sentence to /output/entry.txt: an explanation of the modern
internet for someone who has just stepped out of the year 1800, using
only words and things a person from that year already knows.

The sentence is a single comparison, and the comparison is true of the
internet as it is: every door on earth now opens onto every other door.
Through those doors you may speak with any soul alive and read any book
ever written, without leaving your chair -- the distance is gone, the
talking is two-way, and the books are all at hand. No word in it was
coined after 1800, no feature is listed, and the one image -- doors
opening onto doors -- is the whole picture.
"""

import os
from pathlib import Path

TEXT = (
    "Every door on earth now opens onto every other door, so you may "
    "speak with any soul alive and read any book ever written without "
    "leaving your chair."
)


# The competition accepts texts of 1 to 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
