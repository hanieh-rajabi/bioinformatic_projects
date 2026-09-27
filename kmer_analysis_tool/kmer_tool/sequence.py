def validate_sequence(sequence):
    sequence = sequence.strip().upper()

    if not sequence:
        raise ValueError("sequence can't be empty.")

    valid_bases = {"A", "T", "G", "C"}
    for base in sequence:
        if base not in valid_bases:
            raise ValueError(f"Invalid nucleotide found: {base}")
    return sequence