#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = "I blocked two hours of focus time on my calendar, so my manager booked a meeting titled 'Quick sync about your focus time'."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
