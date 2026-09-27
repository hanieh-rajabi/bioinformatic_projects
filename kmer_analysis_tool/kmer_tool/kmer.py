from collections import Counter
from .sequence import validate_sequence


def generate_kmers(sequence, k):
    sequence = validate_sequence(sequence)

    if type(k) != int: 
        raise TypeError("k must be an integer.")

    if k <= 0:
        raise ValueError("k must be greater than zero.")

    if k > len(sequence):
        raise ValueError("k cannot be larger than the sequence length.")

    kmers = []
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        kmers.append(kmer)
    return kmers


def count_kmers(sequence, k):
    kmers = generate_kmers(sequence, k)
    return Counter(kmers)