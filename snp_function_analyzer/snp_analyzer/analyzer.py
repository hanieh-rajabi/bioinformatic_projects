from .sequence import apply_snp
from .codon import get_codon, translate_codon
from .consequence import classify_consequence


def analyze_snp(sequence, position, reference, alternate):
    mutated_sequence = apply_snp(sequence, position, reference, alternate)
    reference_codon = get_codon(sequence, position)
    alternate_codon = get_codon(mutated_sequence, position)
    reference_aa = translate_codon(reference_codon)
    alternate_aa = translate_codon(alternate_codon)
    consequence = classify_consequence(reference_codon, alternate_codon)

    return {
        "position": position,
        "reference": reference,
        "alternate": alternate,
        "reference_codon": reference_codon,
        "alternate_codon": alternate_codon,
        "reference_aa": reference_aa,
        "alternate_aa": alternate_aa,
        "consequence": consequence
    }
