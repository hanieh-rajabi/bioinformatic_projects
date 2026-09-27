from Bio import SeqIO

fasta_file = "data/TP53_CDS.fasta"
record = SeqIO.read(fasta_file, "fasta")
sequence = record.seq

print("sequence length:", len(sequence))
print("remainder after division by 3:", len(sequence) % 3)

if len(sequence) % 3 != 0:
    raise ValueError("CDS length is not divisible by 3.")

protein = sequence.translate()

print("protein length:", len(protein))
print("last amino acid:", protein[-1])

if protein[-1] != "*":
    raise ValueError("CDS should end with a stop codon.")

print("CDS was checked successfully.")