VALID_BASES = {"A", "T", "G", "C"}


def validate_sequence(sequence):
    sequence = sequence.upper().strip()

    if not sequence:
        raise ValueError("sequence can't be empty.")

    for base in sequence:
        if base not in VALID_BASES:
            raise ValueError(f"Invalid nucleotide: {base}")
    return sequence


def calculate_gc_content(sequence):
    sequence = validate_sequence(sequence)
    gc_count = (sequence.count("G") + sequence.count("C"))
    gc_content = (gc_count / len(sequence)) * 100
    return gc_content