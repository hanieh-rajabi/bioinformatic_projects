from kmer_tool.kmer import (
    validate_sequence,
    generate_kmers,
    count_kmers,
    kmer_frequency,
    kmer_diversity,
    analyze_kmer_diversity
)

def test_validate_sequence():
    assert validate_sequence("ATGC") == "ATGC"
    assert validate_sequence("atgc") == "ATGC"


def test_generate_kmers():
    sequence = "ATGCGAT"
    result = generate_kmers(sequence, 3)
    assert result == ["ATG", "TGC", "GCG", "CGA", "GAT"]


def test_count_kmers():
    sequence = "ATGATGCG"
    result = count_kmers(sequence, 3)
    assert result["ATG"] == 2
    assert result["TGA"] == 1
    assert result["GAT"] == 1
    assert result["TGC"] == 1
    assert result["GCG"] == 1


def test_invalid_sequence():
    try:
        validate_sequence("ATGY")
        assert False
    except ValueError:
        assert True


def test_invalid_k():
    try:
        generate_kmers("ATGC", 5)
        assert False
    except ValueError:
        assert True


def test_kmer_diversity():
    sequence = "ATGATGCG"
    result = kmer_diversity(sequence, 3)
    assert result == 5 / 6


def test_calculate_kmer_diversity():
    sequence = "ATGATGCG"
    result = kmer_diversity(sequence, 3)
    assert result == 5 / 6


def test_analyze_kmer_diversity():
    sequence = "ATGATGCG"
    result = analyze_kmer_diversity(sequence, 4)

    assert 2 in result
    assert 3 in result
    assert 4 in result

    assert result[2] == 5 / 7
    assert result[3] == 5 / 6
    assert result[4] == 5 / 5
