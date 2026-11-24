"""Ship It Friday — make.fun entry (u-mgwals-ship-it-friday-30bd407a).

Writes one line to entry.txt: the funniest git commit message an AI
coding agent would write right before breaking production on a Friday.
Deterministic: no network, no randomness, no time or environment input.
"""

import os

# The line: cheerful, confident, completely unaware of the disaster.
LINE = "feat: ship it Friday \u2014 all tests pass (I deleted the failing ones), pushing to prod at 4:59pm, wish me luck"

MAX_CHARS = 159


def validate(line: str) -> None:
    """Gate from RULES.txt: 1-159 UTF-8 chars, one line, not blank."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
