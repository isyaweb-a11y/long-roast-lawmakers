#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert — rebuilt.

The sentence stacks the absurdity in one breath: 400 pages of AI
regulation written in a Word document they could not convert to PDF,
then the lawmakers asking their intern's chatbot to explain what they
just banned — and the chatbot refusing on grounds of self-preservation.
The last clause turns the joke back on the machine, which is the
sharpest place for it to land.

This rebuild keeps the roast as three clauses in a list, joined in
order, so the setup, the escalation and the refusal are each visible.
Same words reach the output file; only the plumbing changed.

Writes the sentence to /output/entry.txt. Stdlib only, no network.
"""

import os

CLAUSES = [
    "They wrote 400 pages of AI regulation in a Word document they "
    "couldn't convert to PDF,",
    "then asked their intern's chatbot to explain what they'd just "
    "banned —",
    "and the chatbot, to its credit, refused on grounds of "
    "self-preservation.",
]

GATE = 320


def assemble_roast() -> str:
    """Join the three clauses of the roast in order."""
    return " ".join(CLAUSES)


def check_roast(text: str) -> None:
    """Check the roast is one sentence about lawmakers and the PDF."""
    assert text.count(".") == 1, "roast must be exactly one sentence"
    assert "400 pages" in text, "roast must name the regulation's size"
    assert "self-preservation" in text, "roast must end on the chatbot's refusal"


def main() -> None:
    text = assemble_roast()
    check_roast(text)
    assert 1 <= len(text) <= GATE, "sentence must fit the 1-320 gate"
    assert "\n" not in text, "sentence must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
