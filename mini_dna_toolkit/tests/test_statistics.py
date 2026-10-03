from dna_toolkit.statistics import (sequence_length, base_counts, gc_content)


def test_sequence_length():
    assert sequence_length("ATGC") == 4


def test_base_counts():
    counts = base_counts("AATGCC")
    assert counts["A"] == 2
    assert counts["T"] == 1
    assert counts["G"] == 1
    assert counts["C"] == 2


def test_gc_content():
    assert gc_content("ATGC") == 50.0
