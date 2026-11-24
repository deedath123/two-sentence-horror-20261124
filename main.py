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
