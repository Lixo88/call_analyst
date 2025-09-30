"""Inventory indexing script for the call analyst pipeline.

This executable will scan the raw audio and metadata repositories, generate an
index of available calls, and write a manifest into ``data/interim`` for use by
subsequent steps.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the inventory indexing script."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--audio-root",
        type=Path,
        default=Path("data/raw_audio"),
        help="Path to the directory containing raw audio files.",
    )
    parser.add_argument(
        "--metadata-root",
        type=Path,
        default=Path("data/raw_metadata"),
        help="Path to the directory containing metadata files.",
    )
    parser.add_argument(
        "--output-manifest",
        type=Path,
        default=Path("data/interim/inventory_manifest.json"),
        help="Destination for the generated inventory manifest.",
    )
    return parser.parse_args()


def main() -> None:
    """Entrypoint for scanning raw assets and building an inventory manifest."""

    args = parse_args()

    # TODO: Traverse audio and metadata directories, align records, and write a
    # manifest file for downstream pipeline stages.
    raise NotImplementedError


if __name__ == "__main__":
    main()
