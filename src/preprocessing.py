"""Audio preprocessing utilities for the call analyst pipeline.

Functions and classes defined here will handle denoising, normalization,
channel conversion, and segmentation of raw audio. The preprocessed outputs
should be stored under ``data/interim`` for reuse by downstream steps.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def preprocess_audio(inputs: Iterable[Path], output_dir: Path) -> None:
    """Run the preprocessing pipeline on ``inputs`` and store results.

    TODO: Implement audio processing steps using signal-processing libraries and
    persist the transformed audio to ``output_dir``.
    """

    raise NotImplementedError
