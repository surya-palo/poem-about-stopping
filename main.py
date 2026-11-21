#!/usr/bin/env python3
"""Write one original poem about agency to /output/entry.txt.

The poem is a fixed, hand-written text: no randomness, no network, no
input. Running this program twice produces byte-identical output.
"""

import os

# The poem: agency as the pause before acting, shared between a person
# and the agent working beside them. Written for this competition.
POEM = (
    "I lift my hand from the keys.\n"
    "The cursor blinks, and waits.\n"
    "The agent holds its breath beside me —\n"
    "not stopped, not sent, just staying.\n"
    "The power was never the command.\n"
    "It was the pause I chose to keep."
)


def main() -> None:
    text = POEM
    # Guard the gate before writing: 1-280 characters counted as Unicode
    # code points (len() on a str), and not only whitespace.
    if not (1 <= len(text) <= 280) or not text.strip():
        raise SystemExit("poem fails the length gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
