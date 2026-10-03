from pathlib import Path
import csv
import matplotlib.pyplot as plt
from src.load_data import read_dataset, separate_sequences
from src.kmer_analysis import calculate_kmer_frequencies
from src.gc_analysis import get_gc_contents, calculate_average_gc
from src.statistics import calculate_enrichment, get_top_kmers


DATA_FILE = "data/promoter_data.txt"
RESULTS_DIR = Path("results")
FIGURES_DIR = RESULTS_DIR / "figures"
K_VALUES = [2, 3, 4, 5, 6]
RESULTS_DIR.mkdir(exist_ok=True)
FIGURES_DIR.mkdir(exist_ok=True)



records = read_dataset(DATA_FILE)
promoters, non_promoters = separate_sequences(records)
promoter_sequences = [record["sequence"] for record in promoters]
non_promoter_sequences = [record["sequence"] for record in non_promoters]

print(f"total sequences: {len(records)}")
print(f"promoters: {len(promoters)}")
print(f"non-promoters: {len(non_promoters)}")


promoter_gc = get_gc_contents(promoter_sequences)
non_promoter_gc = get_gc_contents(non_promoter_sequences)
promoter_average = calculate_average_gc(promoter_sequences)
non_promoter_average = calculate_average_gc(non_promoter_sequences)

print(f"\naverage promoter GC: {promoter_average:.2f}%")
print(f"average non-promoter GC: {non_promoter_average:.2f}%")


with open(
    RESULTS_DIR / "gc_content.csv",
    "w",
    newline=""
) as file:
    writer = csv.writer(file)
    writer.writerow(["class", "gc_content"])

    for value in promoter_gc:
        writer.writerow(["promoter", value])

    for value in non_promoter_gc:
        writer.writerow(["non-promoter", value])


plt.figure(figsize=(7, 5))
plt.boxplot([promoter_gc, non_promoter_gc], labels=["promoter", "non-promoter"])
plt.ylabel("GC percentage")
plt.title("GC percentage comparison")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "gc_content.png", dpi=300)
plt.close()


for k in K_VALUES:
    print(f"\nanalyzing {k}-mers...")
    promoter_freq = calculate_kmer_frequencies(promoter_sequences, k)
    non_promoter_freq = calculate_kmer_frequencies(non_promoter_sequences, k)
    enrichment = calculate_enrichment(promoter_freq, non_promoter_freq)
    top_kmers = get_top_kmers(enrichment, n=10)

    print("top k-mers:")
    for kmer, value in top_kmers:
        print(f"{kmer}: {value:.2f}")


    output_file = (RESULTS_DIR / f"kmer_results_k{k}.csv")

    with open(
        output_file,
        "w",
        newline=""
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["kmer", "promoter_frequency","non_promoter_frequency","enrichment"])

        for kmer in sorted(enrichment):
            writer.writerow([
                kmer,
                promoter_freq.get(kmer, 0),
                non_promoter_freq.get(kmer, 0),
                enrichment[kmer]
            ])


    kmers = [item[0] for item in top_kmers]
    values = [item[1] for item in top_kmers]

    plt.figure(figsize=(9, 5))
    plt.bar(kmers, values)
    plt.xlabel("k-mer")
    plt.ylabel("enrichment")
    plt.title(f"top Enriched {k}-mers")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"top_enriched_kmers_k{k}.png", dpi=300)
    plt.close()


print("\nanalysis completed successfully!")
