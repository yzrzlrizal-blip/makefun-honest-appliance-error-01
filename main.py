"""The Funniest Honest Appliance Error — make.fun entry.

Writes one line (at most 200 characters): the funniest honest error
message an appliance could show. Pure standard library, deterministic.

The sealed gate accepts UTF-8 text of 1 to 200 characters, so the program
refuses to write a line outside that range and verifies the file bytes
it just wrote before exiting.
"""

import os
import sys

LINE = "ERROR: I burned your toast again. The dial said 3. I do not know what 3 means either."


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"entry line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE:
        print("entry line must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != LINE + "\n":
        print("verification failed: entry.txt does not match the line", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)}-char entry to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
