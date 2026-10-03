from collections import Counter
from .seq_utils import validate_sequence


def generate_kmers(sequence, k):
    sequence = validate_sequence(sequence)

    if k <= 0:
        raise ValueError("k must be greater than zero.")

    if k > len(sequence):
        raise ValueError("k can't be greater than the length of the sequence.")

    kmers = []
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        kmers.append(kmer)
    return kmers


def count_kmers(sequence, k):
    kmers = generate_kmers(sequence, k)
    counts = Counter(kmers)
    return counts


def calculate_kmer_frequencies(sequences, k):
    total_counts = Counter()

    for sequence in sequences:
        counts = count_kmers(sequence, k)
        total_counts.update(counts)

    total_kmers = sum(total_counts.values())

    if total_kmers == 0:
        return {}

    frequencies = {}

    for kmer, count in total_counts.items():
        frequencies[kmer] = (count / total_kmers)

    return frequencies