"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single sentence to $MAKEFUN_OUTPUT_DIR/entry.txt that
convinces a friend who has never coded to let an AI agent build
their first app idea on make.fun.

Pure stdlib, deterministic, no network, no clock, no randomness.
"""

import os

PITCH = (
    "Just tell it your idea in plain words, like you'd tell me, "
    "and it builds the app while you watch \u2014 nothing to install, "
    "nothing to learn first, and it's still your idea when it's done."
)


def main() -> None:
    # Gate guard: the sealed gate requires 1-240 chars; keep a margin
    # so the entry passes even counting the trailing newline.
    assert 1 <= len(PITCH) <= 230, "pitch out of length bounds"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
