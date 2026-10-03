from .sequence import valid_sequence


def transcribe(sequence: str) -> str:
    sequence = valid_sequence(sequence)
    return sequence.replace("T", "U")
