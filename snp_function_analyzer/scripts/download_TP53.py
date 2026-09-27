from Bio import Entrez, SeqIO
from pathlib import Path


Entrez.email = "rajabi.hanieh@gmail.com"
accession = "NM_000546.6"
handle = Entrez.efetch(
    db="nuccore",
    id=accession,
    rettype="gb",
    retmode="text"
)
record = SeqIO.read(handle, "genbank")
handle.close()

print("accession:", record.id)
print("description:", record.description)
print("sequence length:", len(record.seq))

for feature in record.features:
    if feature.type == "CDS":
        cds = feature.extract(record.seq)

        print("CDS found!")
        print("CDS location:", feature.location)
        print("CDS length:", len(feature.extract(record.seq)))

        output_file = Path("data/TP53_CDS.fasta")

        with open(output_file, "w") as file:
            file.write(">TP53_NM_000546.6_CDS\n")
            file.write(str(cds))

        print("CDS saved to:", output_file)