import pytest
from dna_toolkit.transcription import transcribe


def test_transcription():
    assert transcribe("ATGC") == "AUGC"


def test_lowercase_sequence():
    assert transcribe("atgc") == "AUGC"


def test_sequence_with_spaces():
    assert transcribe("ATG C") == "AUGC"


def test_invalid_sequence():
    with pytest.raises(ValueError):
        transcribe("ATGX")
