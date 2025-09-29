"""Batch transcription script for the call analyst pipeline.

This executable will load the inventory manifest, dispatch audio segments to
an automatic speech recognition backend, and store transcripts in
``data/processed``.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the transcription script."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--inventory-manifest",
        type=Path,
        default=Path("data/interim/inventory_manifest.json"),
        help="Path to the manifest of audio assets to transcribe.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/processed/transcripts"),
        help="Directory where generated transcripts should be written.",
    )
    parser.add_argument(
        "--model-name",
        type=str,
        default="whisper-large-v3",
        help="Identifier for the transcription model or service to use.",
    )
    return parser.parse_args()


def main() -> None:
    """Entrypoint for performing batch transcription based on an inventory."""

    args = parse_args()

    # TODO: Load the manifest, perform audio preprocessing as needed, submit
    # transcription jobs, and persist transcripts with metadata for analysis.
    raise NotImplementedError


if __name__ == "__main__":
    main()
