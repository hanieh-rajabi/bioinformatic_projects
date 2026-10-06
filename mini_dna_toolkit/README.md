# Mini DNA Toolkit

A small python package with the basic DNA operations you meet in the first weeks of a molecular biology or bioinformatics course. I wrote it to practise turning textbook rules (base pairing, the genetic code, start and stop codons) into code, and to learn how to structure a package and test it with pytest.

It only uses the python standard library.

## What it can do

| Module | Functions | Notes |
|---|---|---|
| `sequence.py` | `valid_sequence`, `reverse_complement` | uppercases input, strips spaces and newlines, rejects anything that isn't A/T/G/C |
| `statistics.py` | `sequence_length`, `base_counts`, `gc_content` | GC content is returned as a percentage |
| `transcription.py` | `transcribe` | DNA to RNA (T to U) |
| `translation.py` | `translate` | Standard genetic code. Stops at the first stop codon by default, or keeps going with `stop_at_stop=False` |
| `orf.py` | `find_orf` | Finds the first ATG and reads in frame until a stop codon, returns the protein |

## Quick example

```python
from dna_toolkit.sequence import valid_sequence, reverse_complement
from dna_toolkit.transcription import transcribe
from dna_toolkit.translation import translate
from dna_toolkit.orf import find_orf

dna = valid_sequence("cccatggccatctaa")
print(reverse_complement(dna))           # TTAGATGGCCATGGG
print(transcribe(dna))                   # CCCAUGGCCAUCUAA
print(find_orf(dna))                     # MAI*
```

The same thing is in `example/basic_example.py`. Run it from the `mini_dna_toolkit` folder as a module so Python can find the package:

```bash
python -m example.basic_example
```

## Tests

```bash
pip install pytest
python -m pytest
```


## Project structure

```text
mini_dna_toolkit/
├── dna_toolkit/
│   ├── sequence.py
│   ├── statistics.py
│   ├── transcription.py
│   ├── translation.py
│   └── orf.py
├── example/
│   └── basic_example.py
├── notebooks/
│   └── 01_sequence_basics.ipynb
└── tests/
```

## Limitations

- `find_orf` only looks at the first ATG on the forward strand. If that ATG has no in-frame stop, it returns `None` even when a later ATG would give a valid ORF.
- Only the standard genetic code is supported.
- Ambiguous bases like `N` are rejected rather than handled.

## Ideas for improvement

- Search all three forward frames and the three reverse-complement frames, and return every ORF above a minimum length instead of just the first one.
- Add FASTA reading so the functions can run on real files, not only strings.
- Allow `N` and other IUPAC codes in validation, with an option to keep or drop them.
- Add a `pyproject.toml` so the package can be installed with `pip install -e .`. That would also fix the import issue with plain `pytest` and the example script.
- Compare results against Biopython (`Seq.reverse_complement()`, `Seq.translate()`) in the tests as a sanity check.
- Add a small CLI, for example `python -m dna_toolkit gc sequence.fasta`.
