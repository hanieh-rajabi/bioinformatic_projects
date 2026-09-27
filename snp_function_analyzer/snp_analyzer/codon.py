from Bio.Data import CodonTable


table = CodonTable.unambiguous_dna_by_name["Standard"]

def get_codon(sequence, position):
    index = position - 1
    codon_start = (index // 3) * 3
    codon_end = codon_start + 3

    if codon_end > len(sequence):
        raise ValueError("SNP is located in an incomplete codon.")

    return sequence[codon_start:codon_end]


def translate_codon(codon):
    codon = codon.upper()

    if codon in table.stop_codons:
        return "*"

    if codon not in table.forward_table:
        raise ValueError(f"Invalid codon: {codon}")

    return table.forward_table[codon]

