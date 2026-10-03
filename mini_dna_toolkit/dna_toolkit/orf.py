from .sequence import valid_sequence
from .transcription import transcribe
from .translation import translate


START_CODON = "AUG"
STOP_CODONS = {"UAA", "UAG", "UGA"}


def find_orf(sequence: str) -> str | None:
    rna = transcribe(valid_sequence(sequence))
    start = rna.find(START_CODON)

    if start == -1:
        return None

    for position in range(start + 3, len(rna) - 2, 3):
        codon = rna[position:position + 3]

        if codon in STOP_CODONS:
            orf = rna[start:position + 3]
            return translate(orf, stop_at_stop=False)

    return None
