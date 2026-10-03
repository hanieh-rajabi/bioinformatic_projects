import pytest
from src.seq_utils import (validate_sequence, calculate_gc_content)
from src.kmer_analysis import (generate_kmers, count_kmers)
from src.statistics import (calculate_enrichment)


def test_validate_sequence():
    sequence = "atgc"
    result = validate_sequence(sequence)
    assert result == "ATGC"


def test_invalid_sequence():
    with pytest.raises(ValueError):
        validate_sequence("ATGX")


def test_gc_content():
    sequence = "GGCTAT"
    result = calculate_gc_content(sequence)
    assert round(result, 2) == 50


def test_generate_kmers():
    sequence = "ATGC"
    result = generate_kmers(sequence, 2)
    assert result == ["AT","TG","GC"]


def test_kmer_count():
    sequence = "AAAA"
    result = count_kmers(sequence, 2)
    assert result["AA"] == 3


def test_enrichment():
    promoter = {"AAA": 0.4}
    non_promoter = {"AAA": 0.1}
    result = calculate_enrichment(promoter, non_promoter)
    assert result["AAA"] > 1