from collections import Counter
from .sequence import valid_sequence


def sequence_length(sequence):
    sequence = valid_sequence(sequence)
    return len(sequence)


def base_counts(sequence):
    sequence = valid_sequence(sequence)
    counts = Counter(sequence)
    return {
        "A": counts["A"],
        "T": counts["T"],
        "G": counts["G"],
        "C": counts["C"]
    }



def gc_content(sequence):
    sequence = valid_sequence(sequence)
    gc_count = sequence.count("G") + sequence.count("C")
    return gc_count / len(sequence) * 100

