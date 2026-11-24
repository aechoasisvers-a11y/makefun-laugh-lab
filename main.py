"""One-Liner Laugh Lab entry.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock. Pure stdlib Python 3.13.
"""

import os

ENTRY_TEXT = "The sock came at me, toe first, at 3 a.m. I stand by my actions."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)

    # Self-check: read the file back and verify it against the gate
    # (UTF-8 text, 1 to 200 characters, not only whitespace, one line,
    # no trailing newline) and against the intended text.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY_TEXT, "output does not match intended entry text"
    assert 1 <= len(written) <= 200, "entry outside the 1-200 char gate"
    assert written.strip() != "", "entry is only whitespace"
    assert "\n" not in written, "entry must be a single line"
    assert not written.endswith("\n"), "no trailing newline allowed"


if __name__ == "__main__":
    main()
