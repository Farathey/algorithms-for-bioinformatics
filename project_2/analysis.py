def compare(non_mutated_seq, mutated_seq):
    '''Function which returns the list (indexed from 0) of positions in which they differ
    Paramters:
    ---------
    non_mutated_seq : str
        Original sequence without mutations
    
    mutated_seq : str
        Sequence which was modified by mutations'''
    # First we check which sequence is longer to avoid going out of range - we will use loop_range as a range in our
    # loop 
    if len(non_mutated_seq) > len(mutated_seq):
        loop_range = len(mutated_seq)
    else:
        loop_range = len(non_mutated_seq)

    # Here we look for positions in which both sequences differ
    i = 0
    positions = []
    for i in range(loop_range):
        if non_mutated_seq[i] != mutated_seq[i]:
            positions.append(i)
        i += 1

    return positions

def reading_frame_change(non_mutated_seq, mutated_seq):
    ''' Function which returns True if change in reading frame occured and False if it didn't
    Paramters:
    ---------
    non_mutated_seq : str
        Original DNA sequence without mutations
    
    mutated_seq : str
        Sequence which was modified by mutations'''
    
    # We check this on the basis of whether there is a difference in len(seq) mod 3 - reading frame reads codon by codon
    # which means triad of nitrogenous bases by triad - so if mod 3 differs it means that reading framed moved by 1 or 2
    # nitrogenous bases
    if len(non_mutated_seq)%3 != len(mutated_seq)%3:
        return True
    else:
        return False

def find_protein(seq):
    '''Returns (if it exists) first found protein in given amino acids seqence. If there aren't any returns -1
    Parameters:
    ----------
    seq : str
        Amino acids sequence in which we are looking for proteins'''

    # Protein is found by first looking for 'M' which is encoded by start codon, and then by looging for
    # '_' in the slice from found 'M' to the end. '_' is encoded by stop codons
    for i in range(len(seq)):
        if seq[i] == 'M':
            for j in range(i, len(seq)):
                if seq[j] == '_':
                    return seq[i : j+1]

    return -1


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TESTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
if __name__ == '__main__':
    assert compare('AAAAAAAAAAAA', 'AACATAAAA') == [2, 4]
    assert reading_frame_change('AAAAAAAAA', 'AAAATC') == False
    assert reading_frame_change('AAAAAAAAA', 'AAAATCAA') == True
    assert find_protein('ADPMKIJF_A') == 'MKIJF_'
    assert find_protein('AAAAAAAAA') == -1