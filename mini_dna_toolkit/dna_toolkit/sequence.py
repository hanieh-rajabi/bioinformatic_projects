VALID_BASES = {"A", "T", "G", "C"}


def valid_sequence(sequence):
    sequence = sequence.upper().replace(" ", "").replace("\n", "")

    if not sequence:
        raise ValueError("DNA sequence can't be empty!")

    invalid_bases = set(sequence) - VALID_BASES

    if invalid_bases:
        raise ValueError(
            f"invalid DNA bases: {', '.join(sorted(invalid_bases))}"
        )
    return sequence


def reverse_complement(sequence):
    sequence = valid_sequence(sequence)
    complement_map = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    complement = ""

    for base in sequence:
        complement += complement_map[base]
    return complement[::-1]
