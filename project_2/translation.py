from sequence_generator import generate_random_sequence

def transcribe_and_translate(dna_seq):
    '''Function which first creates complimenary sequence and than using dictionary from the book "Bioinformatics
    Algorithms" by M. Rocha and R. G. Ferreira translates it to protein sequence which is being returned at the end
    Parameters:
    ----------
    dna_seq : str
        DNA sequence in which we are transcribing and translating'''

    # First we make sure that the whole sequence is in 
    seq = dna_seq.upper()
    # Then we create complimentary sequence - we do not use uracile (U) on puropse (explenation below)
    complimentary_seq = ""
    for i in range(len(seq)):
        if seq[i] == 'A':
            complimentary_seq = complimentary_seq + 'T'
        elif seq[i] == 'T':
            complimentary_seq = complimentary_seq + 'A'
        elif seq[i] == 'G':
            complimentary_seq = complimentary_seq + 'C'
        else:
            complimentary_seq = complimentary_seq + 'G'

    # Here is dictionary from the book. As we can see its not our usual RNA - it was left in DNA format
    # uracile (U) from RNA is replaced with thymine (T) from DNA
    amino_aacids_dict = {
        "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "TGT":"C", "TGC":"C",
        "GAT":"D", "GAC":"D",
        "GAA":"E", "GAG":"E",
        "TTT":"F", "TTC":"F",
        "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",
        "CAT":"H", "CAC":"H",
        "ATA":"I", "ATT":"I", "ATC":"I",
        "AAA":"K", "AAG":"K",
        "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
        "ATG":"M", 
        "AAT":"N", "AAC":"N",
        "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAA":"Q", "CAG":"Q",
        "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
        "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S",
        "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
        "TGG":"W",
        "TAT":"Y", "TAC":"Y",
        "TAA":"_", "TAG":"_", "TGA":"_"}

    # Here we translate our complimentary sequence to protein sequence by grouping it in triads and translateing them
    # according to our dictionary 
    protein_seq = ""
    for i in range(0, len(complimentary_seq), 3):
        codon = complimentary_seq[i : i+3]
        if codon in amino_aacids_dict:
            protein_seq = protein_seq + amino_aacids_dict[codon]
    
    return protein_seq

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TESTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
if __name__ == '__main__':
    test_seq = transcribe_and_translate(generate_random_sequence(42))
    for i in range(len(test_seq)):
        assert test_seq[i] in 'ACDEFGHIKLMNPQRSTVWY_'