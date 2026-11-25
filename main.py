"""Time machine warning label entry for make.fun.

The joke: every time machine ships with one irresistible red button, and the
label finally admits what pressing it "just to see" already cost us — the
dinosaurs. A warning written by whoever had to clean up afterwards.
"""

import os

ENTRY = "WARNING: Do not press the red button to see what it does. That is how we got the dinosaurs."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
