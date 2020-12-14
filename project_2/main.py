''' The package random includes a number of functions that allow to generate random numbers.
Using some of those functions, build a module that implements the generation of
random DNA sequences and the analysis of mutations over these sequences. You can include
functions to generate random sequences of a given size, to simulate the occurrence
of a given number of mutations in a DNA sequence in random positions (including insertions,
deletions, and substitutions), and functions to study the impact of mutations in the
encoded proteins of those sequences. '''

# Here we import everything we need
from sequence_generator import generate_random_sequence
import analysis
import mutations
from translation import transcribe_and_translate
from random import randint
from frequent import frequent_words

# For start we create randomly generated sequence with defalut proporions with length inputed by user
seq_lenght = int(input("Input the lenght of sequence you'd like to generate: "))
sequence = generate_random_sequence(seq_lenght)
mutated_sequence = sequence

# Here we mutate our sequence with randomly draw inputed number of mutations
mutations_num = int(input("Input number of mutations: "))
for i in range(20):
    random_value = randint(1, 3)

    if random_value == 1:
        mutated_sequence = mutations.insertion(mutated_sequence)
    elif random_value == 2:
        mutated_sequence = mutations.deletion(mutated_sequence)
    else:
        mutated_sequence = mutations.subsitution(mutated_sequence)

# Here we print our sequences and start to analyse them
print("Original sequence :", sequence)
print("Mutated sequence  :", mutated_sequence)

# Here we print positions in which mutated sequence differs from original one
print("Sequences differ in positions :", analysis.compare(sequence, mutated_sequence))

# Here we check whether mutated sequence is longer or shorter than the original one, and how great is the difference
if len(sequence) > len(mutated_sequence):
    print("Original sequence is longer by", len(sequence)-len(mutated_sequence), "bases")
else:
    print("Mutated sequence is longer by", len(mutated_sequence)-len(sequence), "bases")

# Here we print whether reading frame changed
print("Did reading frame change?", analysis.reading_frame_change(sequence, mutated_sequence))

# Here we print the most often occuring patterns of given length (ex. 5) in both sequences
pattern_length = 5
print("The most frequent patterns of length", pattern_length, "in original sequence are", frequent_words(sequence, pattern_length))
print("The most frequent patterns of length", pattern_length, "in mutated sequence are", frequent_words(mutated_sequence, pattern_length))

# Here we transcribe and translat sequences to amino acids sequences
amino_acids_seq = transcribe_and_translate(sequence)
mutated_amino_acids_seq = transcribe_and_translate(mutated_sequence)

# Here we print them
print("\nOriginal amino acids sequence :", amino_acids_seq)
print("Mutated amino acids sequence  :", mutated_amino_acids_seq)

# Here we print positions in which mutated amino acids sequence differs from original one
print("Amino acids sequences differ in positions :", analysis.compare(amino_acids_seq, mutated_amino_acids_seq))

# Here we look for proteins in our amino acids sequences and if we find any we print them
protein1 = analysis.find_protein(amino_acids_seq)
protein2 = analysis.find_protein(mutated_amino_acids_seq)
if protein1 == -1:
    print("There is no protein in original sequence")
else:
    print("Protein found in original sequence :", protein1)

if protein2 == -1:
    print("There is no protein in mutated sequence")
else:
    print("Protein found in mutated sequence  :", protein2)
