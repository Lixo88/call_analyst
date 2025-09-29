"""Input/output helpers for working with call audio and metadata files.

This module will provide utilities for discovering available audio recordings,
reading associated metadata, and writing intermediate artifacts in a
consistent format. Functions here should abstract away filesystem layout
under ``data/`` so that higher-level pipeline steps can focus on domain logic.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Iterator


def iter_audio_files(root: Path) -> Iterator[Path]:
    """Yield the paths to audio files contained within ``root``.

    TODO: Support filtering by extension, metadata lookups, and chunking for
    batch processing.
    """

    raise NotImplementedError


def load_metadata(entries: Iterable[Path]) -> Iterable[dict]:
    """Load metadata records associated with ``entries`` of audio files.

    TODO: Connect to a metadata store (CSV, JSON, database) and yield structured
    dictionaries for downstream processing.
    """

    raise NotImplementedError
