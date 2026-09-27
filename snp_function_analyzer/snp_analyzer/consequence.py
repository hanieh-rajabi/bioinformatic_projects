from .codon import translate_codon


def classify_consequence(reference_codon, alternate_codon):
    reference_aa = translate_codon(reference_codon)
    alternate_aa = translate_codon(alternate_codon)

    if reference_aa == alternate_aa:
        return "synonymous"

    if alternate_aa == "*":
        return "nonsense"

    return "missense"


def analyze_codon_change(reference_codon, alternate_codon):
    reference_aa = translate_codon(reference_codon)
    alternate_aa = translate_codon(alternate_codon)
    consequence = classify_consequence(reference_codon, alternate_codon)

    return {
        "reference_codon": reference_codon,
        "alternate_codon": alternate_codon,
        "reference_aa": reference_aa,
        "alternate_aa": alternate_aa,
        "consequence": consequence
    }
