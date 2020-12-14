'''Write a function that reads a file in the FASTA format and returns a list with all sequences.'''

from read import read_fasta

# Here we use our function and print out what is returned by it
print(read_fasta(".\\Yersinia_pestis.txt"))
