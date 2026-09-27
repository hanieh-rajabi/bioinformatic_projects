import matplotlib.pyplot as plt


def plot_kmer_diversity(results):
    k_values = list(results.keys())
    diversity_values = list(results.values())

    plt.figure(figsize=(8, 5))
    plt.plot(k_values, diversity_values, marker="o")
    plt.xlabel("k")
    plt.ylabel("K-mer diversity")
    plt.title("K-mer diversity vs. k")
    plt.ylim(0, 1.0)
    plt.show()