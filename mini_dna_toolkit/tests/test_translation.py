from dna_toolkit.translation import translate


def test_translate_single_codon():
    assert translate("AUG") == "M"


def test_translate_multiple_codons():
    assert translate("AUGGCC") == "MA"


def test_translate_stops_at_stop_codon():
    assert translate("AUGGCCUAA") == "MA"


def test_translate_includes_stop_codon():
    assert translate("AUGGCCUAA", stop_at_stop=False) == "MA*"


def test_translate_lowercase_sequence():
    assert translate("auggcc") == "MA"
