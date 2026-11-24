#!/usr/bin/env python3
"""Entry for make.fun bounty u-eager-stork-81-9647-funniest-time-machine-warning-f8add151:
"Funniest Time Machine Warning Label".

Writes one funny single-line warning label for a time machine to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3, standard library only. Deterministic: same bytes every run.

Draft line (first attempt, plain paradox joke):
"WARNING: Do not meet your past self. He will ask to borrow money, and
you already know you will never pay it back."
It names the hazard (meeting your past self) but states the punchline
flatly and wastes words ("will ask to borrow money, and you already
know you will never pay it back" is loose).

Revision (final): reframe the hazard as a lending warning, keep the
official "WARNING:" straight face, and save the surprise for the last
three words — the borrower and the lender are the same person, and the
borrower was present for the whole con. "He was there" turns the loan
into a paradox you cannot escape: you cannot collect from yourself,
because you already watched yourself not pay.
"""

import os

ENTRY = (
    "WARNING: Never lend money to your past self. He already knows he "
    "won't pay you back \u2014 he was there."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
