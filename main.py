#!/usr/bin/env python3
"""Write the chosen developer-excuse entry to entry.txt.

Stdlib only. Deterministic: the same bytes on every run, no trailing
newline, no timestamps, no randomness, no network, no reading of any
other file. The entry lives in this file, which locates itself via
__file__ so the script never depends on the working directory.
"""

import os
from pathlib import Path

ENTRY = "Prod didn't break: it finally ran the code path my tests were too polite to touch."

# The script's own directory, resolved from __file__, not from cwd.
# Used as the fallback output location if /output is unavailable.
SELF_DIR = Path(__file__).resolve().parent


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(ENTRY.encode("utf-8"))
    except OSError:
        fallback = SELF_DIR / "entry.txt"
        fallback.write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
