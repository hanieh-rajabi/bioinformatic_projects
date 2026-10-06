# SNP Function Analyzer

Takes a single-nucleotide variant in a coding sequence and works out what it does to the protein: which codon changes, which amino acid it becomes, and whether the change is synonymous, missense or nonsense.

I used the human **TP53** coding sequence (transcript NM_000546.6) because it's one of the most studied cancer genes and there are plenty of well-documented variants to test against.

## How it works

```text
TP53 CDS (FASTA)
  → check the reference base matches the sequence
  → apply the substitution
  → find the affected codon (reference and alternate)
  → translate both with the standard genetic code
  → classify: synonymous / missense / nonsense
  → save to CSV
```

Positions are 1-based CDS coordinates, the same as the `c.` numbering in HGVS (so `c.215C>G` means position 215, C to G).

## Example variants

| Variant | HGVS | Codon | Amino acid | Result |
|---|---|---|---|---|
| rs1042522 | c.215C>G | CCC → CGC | P → R (Pro72Arg) | missense |
| rs55863639 | c.375G>A | ACG → ACA | T → T (Thr125=) | synonymous |
| rs1555526097 | c.499C>T | CAG → TAG | Q → * (Gln167Ter) | nonsense |

rs1042522 is the well-known P72R polymorphism. The c.375G>A variant is a nice example of where a codon-only view isn't enough. It is synonymous at the protein level, but it sits on the last base of exon 4 and has been reported to disrupt splicing.

## How to run

```bash
pip install -r requirements.txt

python scripts/download_TP53.py   
python scripts/check_cds.py       
python main.py                    
```

Run everything from inside `snp_function_analyzer/`. The CDS is already in `data/`, so the download step is only needed to refresh it. If you do run it, change `Entrez.email` in the script to your own email, because NCBI asks for one.



## Limitations

- Only single-base substitutions inside the CDS. Indels, UTR, intronic and splice-site variants aren't handled.
- The variants are currently written directly in `main.py`. `data/variants.csv` has the same three variants but isn't read yet.
- Stop-lost changes (a stop codon turning into an amino acid) are labelled as missense.


