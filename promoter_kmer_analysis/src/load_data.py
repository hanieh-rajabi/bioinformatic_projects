def read_dataset(filename):

    records = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 3:
                continue

            label = parts[0].strip()
            name = parts[1].strip()
            sequence = parts[2].strip().upper()

            record = {
                "label": label,
                "name": name,
                "sequence": sequence
            }
            records.append(record)
    return records


def separate_sequences(records):
    promoters = []
    non_promoters = []

    for record in records:
        if record["label"] == "+":
            promoters.append(record)

        elif record["label"] == "-":
            non_promoters.append(record)
    return promoters, non_promoters