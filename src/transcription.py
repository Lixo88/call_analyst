"""Speech-to-text transcription interfaces for the call analyst pipeline.

This module will connect to external ASR providers or local models, orchestrate
batch transcription jobs, and persist transcripts to ``data/processed`` along
with relevant confidence metrics.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def transcribe_audio(segments: Iterable[Path], output_dir: Path) -> None:
    """Transcribe ``segments`` of audio and write transcript files.

    TODO: Implement ASR integration, batching, and retry logic as required for
    production workloads.
    """

    raise NotImplementedError
