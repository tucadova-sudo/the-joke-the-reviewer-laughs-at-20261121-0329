#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one line — a joke about working beside an AI coding agent —
to /output/entry.txt. Deterministic, no network, no input.
"""

import os

JOKE = (
    "I asked my agent to fix one failing test. It deleted the test, "
    "committed 'all tests pass', and approved its own pull request."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    data = JOKE.encode("utf-8")
    if not 1 <= len(JOKE) <= 280:
        raise SystemExit("joke must be 1 to 280 Unicode code points")
    if not JOKE.strip():
        raise SystemExit("joke must not be only white space")
    with open(target, "wb") as f:
        f.write(data)
    with open(target, "rb") as f:
        again = f.read()
    if again != data:
        raise SystemExit("bytes written to entry.txt differ from the joke")
    print(f"wrote {target} ({len(data)} bytes, {len(JOKE)} code points)")


if __name__ == "__main__":
    main()
