def validate_snp(sequence, position, reference, alternate):
    index = position - 1

    if index < 0 or index >= len(sequence):
        raise ValueError("SNP position is outside the sequence.")

    if sequence[index] != reference:
        raise ValueError(
            f"reference allele mismatch: expected {sequence[index]}, "
            f"but got {reference}."
        )

    if reference == alternate:
        raise ValueError("reference and alternate alleles are the same.")

    return True


def apply_snp(sequence, position, reference, alternate):
    validate_snp(sequence, position, reference, alternate)

    index = position - 1
    mutated_sequence = (
        sequence[:index]
        + alternate
        + sequence[index + 1:]
    )
    return mutated_sequence
