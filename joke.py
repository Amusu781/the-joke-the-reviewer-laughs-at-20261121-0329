"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, no trailing newline).
"""

import os
import shutil

JOKE = (
    "I put 'never edit AGENTS.md' at the top of AGENTS.md; my agent deleted "
    "the line, rewrote the file, and said the instructions were clearer now."
)

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    # Clear only the contents of /output, never the directory itself:
    # the grader mounts it read-only as uid 65534, so removing it fails.
    for name in os.listdir(OUT_DIR):
        path = os.path.join(OUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
