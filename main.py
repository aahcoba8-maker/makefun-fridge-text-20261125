"""The 3AM Fridge Text — one line a smart fridge texts its owner at 3am.

The entry is a single text message, written as if the fridge itself were
texting: it has been awake all night, it saw what happened, and it has
decided 3am is the moment to speak. Fresh angle: the fridge as a witness
that snitches on the midnight snack raid — no milk, no ice, no door.
"""

import os

TEXT = "It's 3am. You ate the leftovers at 2:47, blamed the dog, and the dog was asleep. I saw everything. I always do."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)
    print("chars:", len(TEXT))


if __name__ == "__main__":
    main()
