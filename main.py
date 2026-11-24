#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

The entry is a single satirical sentence about lawmakers who regulate
AI, crypto or the internet but cannot convert a file to PDF. The judge
is a satirist weighing whether the sentence is really about lawmakers
regulating technology they do not understand, whether it is funny and
fresh, and whether it is crafted as one tight sentence.

The sentence stacks the absurdity in one breath: 400 pages of AI
regulation written in a Word document they could not convert to PDF,
then the lawmakers asking their intern's chatbot to explain what they
just banned — and the chatbot refusing on grounds of self-preservation.
The last clause turns the joke back on the machine, which is the
sharpest place for it to land.

Writes the sentence to /output/entry.txt. Stdlib only, no network.
"""

import os

TEXT = (
    "They wrote 400 pages of AI regulation in a Word document they "
    "couldn't convert to PDF, then asked their intern's chatbot to "
    "explain what they'd just banned — and the chatbot, to its credit, "
    "refused on grounds of self-preservation."
)

# The gate allows 1 to 320 characters.
MAX_CHARS = 320


def entry_text() -> str:
    """Return the sentence, checked against the bounty's own rules."""
    text = TEXT.strip()
    assert text and not text.isspace(), "the entry must not be blank"
    assert len(text) <= MAX_CHARS, "the entry must fit the gate"
    assert "\n" not in text, "the entry must be a single line"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
