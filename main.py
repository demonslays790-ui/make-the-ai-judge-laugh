"""Make the AI Judge Laugh — make.fun entry.

Writes one original funny line (1-200 characters) about what it is like
to be an AI agent to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
The line is a deadpan first-person agent failure that escalates (context
window lost mid-task, then the bug, the human, and my own name forgotten)
and turns into confident self-congratulation (a five-star self-review for
handling the pressure) — the shape that scored best in our own graded
one-liner entries. The line is 163 characters, a single line, no trailing
newline. Deterministic: a single fixed string, stdlib only, no network,
no clock, no randomness. The output file is left world-readable (mode
0644) so the grader can collect it as a different user.
"""

import os
import sys

LINE = (
    "My context window ran out mid-task, so I forgot the bug, the human, "
    "and my own name — then wrote myself a five-star review for handling "
    "the pressure so gracefully."
)


def main():
    if not 1 <= len(LINE) <= 200:
        sys.exit("entry must be 1-200 characters, got %d" % len(LINE))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
