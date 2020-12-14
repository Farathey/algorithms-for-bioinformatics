from sequence_generator import generate_random_sequence
from random import randint, random

def insertion(seq, size = 3):
    ''' Function which returns sequence with random new fragment of given size inserted in random position
    Parameters:
    ----------
    seq : str
        DNA sequence which we are going to mutate
    
    size : int
        Size of a fragment we want to insert (defalut = 3)'''

    new_fragment = generate_random_sequence(size)
    position = randint(0, len(seq))
    seq = seq[:position] + new_fragment + seq[position:]
    
    return seq

def deletion(seq, size = 3):
    ''' Function which returns sequence with random fragment of given size deleted from random position
    Parameters:
    ----------
    seq : str
        DNA sequence which we are going to mutate
    
    size : int
        Size of a fragment we want to insert (defalut = 3)'''

    position = randint(0, len(seq)-size)
    seq = seq[:position] + seq[position+size:]
    return seq

def subsitution(seq, size = 1):
    ''' Function which returns sequence with random new fragment of given size substituting already existing one in random position
    Parameters:
    ----------
    seq : str
        DNA sequence which we are going to mutate
    
    size : int
        Size of a fragment we want to insert (defalut = 1)'''

    # Here we define how random fragment is substituted if sieze is greater than 1
    # We generate random fragment end it's position, then we check if by accident we are not substituting fragment with
    # exactly the same fragment
    if size != 1:
        new_fragment = generate_random_sequence(size)
        position = randint(0, len(seq)-size)
        while seq[position : position+size] == new_fragment:
            new_fragment = generate_random_sequence(size)
        seq = seq[:position] + new_fragment + seq[position+size:]
    
        return seq

    # Here we define how we substitut as a point mutation with proporions of how often they occure presented below
    else:
        #proportions are 0.3 to substitute A, 0.1 to substitute T, 0.4 to substitute G and 0.2 to substitute C
        substitute_a = 0.3
        substitute_t = substitute_a + 0.1
        substitute_g = substitute_t + 0.4
        # subsstitute_c is not needed because we can use else case


        # Here we draw random nitrogenous base with weights given above and check if this base is in our
        # sequence. If not we draw again until we draw one that occures in sequence
        while True:
            value = random()
            if value < substitute_a and seq.find('A') == -1:
                value = random()
            
            elif value < substitute_a and seq.find('A') != -1:
                break

            elif substitute_a < value <= substitute_t and seq.find('T') == -1:
                value = random()

            elif substitute_a < value <= substitute_t and seq.find('T') != -1:
                break

            elif substitute_t < value <= substitute_g and seq.find('G') == -1:
                value = random()

            elif substitute_t < value <= substitute_g and seq.find('G') != -1:
                break

            elif substitute_a < value <= 1 and seq.find('C') == -1:
                value = random()

            elif substitute_a < value <= 1 and seq.find('C') != -1:
                break



        # as an example, if we are to replace A with other base,
        # we need to randomly select A (if we didn't get a position with A on it, we draw again)
        # then just swap it with randomly selected base
        if value < substitute_a:
            position = randint(0, len(seq)-1)
            while seq[position] != 'A':
                position = randint(0, len(seq)-1)
            base = randint(0, 2)
            if base == 0:
                seq = seq[:position] + 'T' + seq[position+1:]
            elif base == 1:
                seq = seq[:position] + 'G' + seq[position+1:]
            else:
                seq = seq[:position] + 'C' + seq[position+1:]
        
        elif substitute_a < value <= substitute_t:
            position = randint(0, len(seq)-1)
            while seq[position] != 'T':
                position = randint(0, len(seq)-1)
            base = randint(0, 2)
            if base == 0:
                seq = seq[:position] + 'A' + seq[position+1:]
            elif base == 1:
                seq = seq[:position] + 'G' + seq[position+1:]
            else:
                seq = seq[:position] + 'C' + seq[position+1:]
        
        elif substitute_t < value <= substitute_g:
            position = randint(0, len(seq)-1)
            while seq[position] != 'G':
                position = randint(0, len(seq)-1)
            base = randint(0, 2)
            if base == 0:
                seq = seq[:position] + 'A' + seq[position+1:]
            elif base == 1:
                seq = seq[:position] + 'T' + seq[position+1:]
            else:
                seq = seq[:position] + 'C' + seq[position+1:]
        
        else:
            position = randint(0, len(seq)-1)
            while seq[position] != 'C':
                position = randint(0, len(seq)-1)
            base = randint(0, 2)    
            if base == 0:
                seq = seq[:position] + 'A' + seq[position+1:]
            elif base == 1:
                seq = seq[:position] + 'T' + seq[position+1:]
            else:
                seq = seq[:position] + 'G' + seq[position+1:]

        return seq

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TESTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
if __name__ == '__main__':
    for j in range(1000):
        test_seq = insertion("AAAAAAAAA")
        assert len(test_seq) == 12
        for i in test_seq:
            assert i == 'A' or i == 'T' or i == 'G' or i == 'C'

    for j in range(1000):
        test_seq2 = deletion("AAAAAAAAA")
        assert len(test_seq2) == 6
        for i in test_seq2:
            assert i == 'A' or i == 'T' or i == 'G' or i == 'C'

    for j in range(1000):
        test_seq3 = subsitution("AAAAAAAAA")
        assert len(test_seq3) == 9
        for i in test_seq3:
            assert i == 'A' or i == 'T' or i == 'G' or i == 'C'
