from Bio import SeqIO
from snp_analyzer.analyzer import analyze_snp
import pandas as pd

fasta_file = "data/TP53_CDS.fasta"

record = SeqIO.read(
    fasta_file,
    "fasta"
)

sequence = record.seq


variants = [
    ("rs1042522", 215, "C", "G"),
    ("rs55863639", 375, "G", "A"),
    ("rs1555526097", 499, "C", "T"),
]


results = []

for variant_id, position, reference, alternate in variants:
    result = analyze_snp(
        sequence=sequence,
        position=position,
        reference=reference,
        alternate=alternate
    )

    result["variant_id"] = variant_id
    results.append(result)


results_df = pd.DataFrame(results)
results_df = results_df[
    [
        "variant_id",
        "position",
        "reference",
        "alternate",
        "reference_codon",
        "alternate_codon",
        "reference_aa",
        "alternate_aa",
        "consequence"
    ]
]


results_df.to_csv(
    "results/snp_results.csv",
    index=False
)

print("results saved to results/snp_results.csv")
print(results_df)


