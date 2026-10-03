from .seq_utils import calculate_gc_content


def get_gc_contents(sequences):
    gc_values = []
    for sequence in sequences:
        gc = calculate_gc_content(sequence)
        gc_values.append(gc)
    return gc_values


def calculate_average_gc(sequences):
    gc_values = get_gc_contents(sequences)

    if not gc_values:
        return 0

    average = sum(gc_values) / len(gc_values)

    return average