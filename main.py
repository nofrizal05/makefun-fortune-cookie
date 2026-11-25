"""Fortune Cookie for the Liquidated Trader.

Writes exactly one fortune-cookie line for a trader who just got
liquidated to entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

LINE = (
    "Your leverage was liquidated, not your luck \u2014 the chart lied, "
    "the margin call collected, and the next candle is still yours."
)

MAX_CHARS = 170


def validate(line):
    """Enforce the one-line gate: non-empty, <=170 chars, no newline."""
    if not line:
        raise ValueError("fortune line must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError("fortune line exceeds 170 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune line must not contain a newline")


def main():
    validate(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    # Read the file back and confirm it holds exactly one line + newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    if content != LINE + "\n":
        raise ValueError("entry.txt does not contain exactly the fortune line")


if __name__ == "__main__":
    main()
