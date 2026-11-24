"""Two-sentence horror entry for make.fun bounty u-suroto-two-sentence-horror-acea9253.

Writes the locked entry text to entry.txt in the output directory.

Verified numbers:
- Entry: exactly two sentences, 208 chars, 208 bytes (UTF-8, no trailing newline)
- entry.txt sha256: 0d21814e75882b26900b58b562ece21f8be62375257e72fdf0df8d01e16f608d
"""

import os

ENTRY = "I tucked both my children into bed at nine and read them the same story I read every night. When I finished, the one on the left asked me to read it again, and the one on the right asked who I was talking to."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
