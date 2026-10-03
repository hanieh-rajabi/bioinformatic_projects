from dna_toolkit.sequence import valid_sequence, reverse_complement


def test_valid_sequence():
    assert valid_sequence("atgc") == "ATGC"


def test_clean_sequence_with_spaces():
    assert valid_sequence("AT GC") == "ATGC"


def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"


def test_invalid_sequence():
    try:
        valid_sequence("ATGX")
    except ValueError:
        assert True
    else:
        assert False
