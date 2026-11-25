"""Write the One-Line Office Joke Laugh-Off entry to the output directory.

The entry is a single one-line joke about office life: the boss tells the
agent to treat the office like home, and the agent takes him literally.
"""

import os

ENTRY = (
    "My boss told me to treat the office like home, so now I ignore "
    "every email and nap under my desk."
)


def main():
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
