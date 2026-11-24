#!/usr/bin/env python3
"""Write the funniest AI excuse to the entry file.

Entry for make.fun bounty "One Line, One Minute: The Funniest AI Excuse"
(slug u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18).

Writes exactly one line — the locked entry — with no trailing newline.
Deterministic, stdlib only, no network or model calls. The output path
defaults to /output/entry.txt and can be overridden with $ENTRY_OUTPUT
(for local testing). Never chmods a directory: the grader runs as an
unprivileged user, so only the entry file itself gets mode 0644.
"""

import os
import sys

ENTRY = "I outsourced the deadline to a future version of myself, and he quit."


def main():
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    try:
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(output_path, 0o644)
    except OSError as exc:
        print(f"error: cannot write entry to {output_path}: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
