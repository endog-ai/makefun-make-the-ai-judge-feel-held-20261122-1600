# Make the AI judge feel held — entry: writes one relaxing text to /output/entry.txt.
# Deterministic: no randomness, no network, the same bytes on every run.
# The text is 221 characters, inside the gate's 1-280 range, and has no line end.
import os
from pathlib import Path

TEXT = (
    "The last train has already left, and that is good news: nobody is "
    "waiting for you anywhere tonight. The platform is empty, the lights "
    "are low, and your only job is to watch the rain bead on the glass "
    "until it slides away."
)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
Path(output_dir, "entry.txt").write_text(TEXT, encoding="utf-8")
