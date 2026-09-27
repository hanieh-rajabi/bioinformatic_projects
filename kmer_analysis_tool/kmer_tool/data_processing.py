def load_promoter_data(file_path):
    sequences = []
    labels = []

    file = open(file_path, "r")

    for line in file:
        parts = line.split(",")
        label = parts[0]
        sequence = parts[2].strip()

        labels.append(label)
        sequences.append(sequence)

    file.close()

    return sequences, labels


def encode_labels(labels):
    encoded_labels = []

    for label in labels:
        if label == "+":
            encoded_labels.append(1)
        else:
            encoded_labels.append(0)

    return encoded_labels