print("basic_example.py is running...")
from dna_toolkit.sequence import valid_sequence, reverse_complement
from dna_toolkit.transcription import transcribe
from dna_toolkit.translation import translate
from dna_toolkit.orf import find_orf


sequence = "CCCATGGCCATCTAA"

valid = valid_sequence(sequence)

print("DNA:", valid)
print("reverse complement:", reverse_complement(valid))

rna = transcribe(valid)
print("RNA:", rna)

print("protein:", translate(rna, stop_at_stop=False))
print("ORF:", find_orf(valid))
