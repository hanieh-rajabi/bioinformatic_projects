def calculate_enrichment(promoter_frequencies, non_promoter_frequencies): #this function accepts dictionaries as inputs
    all_kmers = set(promoter_frequencies) | set(non_promoter_frequencies)

    enrichment = {}

    for kmer in all_kmers:
        promoter_value = (promoter_frequencies.get(kmer, 0))
        non_promoter_value = (non_promoter_frequencies.get(kmer, 0))
        non_promoter_value += 1e-9 #to avoid getting zero devision error
        ratio = promoter_value / non_promoter_value
        enrichment[kmer] = ratio
    return enrichment


def get_top_kmers(enrichment, n=10):
    items = list(enrichment.items())

    items.sort(
        key=lambda x: x[1],
        reverse=True
    )
    top_kmers = items[:n]
    return top_kmers   