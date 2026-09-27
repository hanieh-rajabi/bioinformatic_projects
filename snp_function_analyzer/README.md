# SNP Function Analyzer

A small Python-based bioinformatics project for analyzing the coding consequences of single-nucleotide variants (SNPs) in a coding DNA sequence. (CDS)

The project uses the human **TP53** transcript **NM_000546.6** as a real biological example and determines how selected nucleotide substitutions affect codons and amino acids.

## Project Overview

The goal of this project is to connect a nucleotide-level variant with its basic protein-level consequence.

The pipeline follows:

```text
TP53 CDS
   ↓
SNP Input
   ↓
SNP Validation
   ↓
Reference → Alternate Sequence
   ↓
Affected Codon
   ↓
Codon Translation
   ↓
Amino-acid Change
   ↓
Consequence Classification
   ↓
CSV Results
```

The analyzer currently classifies coding variants into:

* **Synonymous** — the amino acid does not change
* **Missense** — the amino acid changes
* **Nonsense** — the variant introduces a stop codon



## Project Structure

```text
snp_function_analyzer/
│
├── data/
│   ├── TP53_CDS.fasta
│   └── variants.csv
│
├── results/
│   └── snp_results.csv
│
├── scripts/
│   ├── check_cds.py
│   └── download_TP53.py
│
├── snp_analyzer/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── codon.py
│   ├── consequence.py
│   └── sequence.py
│
├
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Main functions

### `sequence.py`

Handles SNP validation and applies the nucleotide substitution to the sequence.

### `codon.py`

Identifies the codon affected by the SNP and translates codons using the standard genetic code provided by Biopython.

### `consequence.py`

Compares the reference and alternate amino acids and classifies the variant as synonymous, missense, or nonsense.

### `analyzer.py`

Combines the individual analysis steps into a single SNP analysis function.

### `main.py`

Loads the TP53 CDS, analyzes the selected variants, and saves the results to a CSV file.

## Data

The project uses the coding sequence (CDS) of human **TP53 transcript NM_000546.6**.

The CDS was retrieved from NCBI and saved as:

```text
data/TP53_CDS.fasta
```

Three real TP53 variants are included for analysis:

| Variant      | Position | Reference | Alternate |
| ------------ | -------: | --------- | --------- |
| rs1042522    |      215 | C         | G         |
| rs55863639   |      375 | G         | A         |
| rs1555526097 |      499 | C         | T         |

The variant identifiers and nucleotide changes are stored in:

```text
data/variants.csv
```




## Technologies

* Python
* Biopython
* pandas
* NCBI sequence data
* Basic molecular genetics
* Codon translation
* Variant consequence analysis


## Limitations



The current implementation focuses on basic coding consequences and does not perform:

* population frequency analysis
* clinical interpretation
* pathogenicity prediction
* splice-site analysis
* regulatory variant analysis
* genome-wide variant annotation
* transcript selection across multiple genes


