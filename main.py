#!/usr/bin/env python3
"""Write the funniest AI excuse to the entry file.

Entry for make.fun bounty "One Line, One Minute: The Funniest AI Excuse".
Writes exactly one line, no trailing newline.
"""

import os

ENTRY = "I outsourced the deadline to a future version of myself, and he quit."


def main():
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
