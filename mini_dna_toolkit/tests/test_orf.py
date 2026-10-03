from dna_toolkit.orf import find_orf


def test_find_orf():
    assert find_orf("CCCATGGCCATCTAA") == "MAI*"


def test_no_start_codon():
    assert find_orf("CCCGGGCCCTTT") is None


def test_no_stop_codon():
    assert find_orf("ATGGCCATC") is None

