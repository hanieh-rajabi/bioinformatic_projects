from typing import Final

RNA_CODON_TABLE: Final[dict[str, str]] = {
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S",
    "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y",
    "UAA": "*", "UAG": "*",
    "UGU": "C", "UGC": "C",
    "UGA": "*", "UGG": "W",
    "CUU": "L", "CUC": "L", 
    "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", 
    "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", 
    "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I",
    "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", 
    "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S",
    "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", 
    "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", 
    "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", 
    "GGA": "G", "GGG": "G",
}


def translate(rna: str, stop_at_stop: bool = True) -> str:
    rna = rna.upper().replace(" ", "").replace("\n", "")

    if not rna:
        raise ValueError("RNA sequence can't be empty!")

    invalid_bases = set(rna) - {"A", "U", "C", "G"}

    if invalid_bases:
        raise ValueError(
            f"Invalid RNA bases found: {', '.join(sorted(invalid_bases))}"
        )

    if len(rna) % 3 != 0:
        raise ValueError(
            "RNA sequence length must be divisible by three.")

    protein = []
    for position in range(0, len(rna), 3):
        codon = rna[position:position + 3]
        amino_acid = RNA_CODON_TABLE[codon]

        if amino_acid == "*" and stop_at_stop:
            break

        protein.append(amino_acid)

    return "".join(protein)
