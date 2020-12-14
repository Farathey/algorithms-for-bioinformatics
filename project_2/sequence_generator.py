from random import random

def generate_random_sequence(size, proportions = [3, 2, 2, 3]):
    '''Function which returns randomly generated DNA sequence of given size
    Parameters:
    ----------
    size : int
        Size of sequence we want to generate
    
    proportions : list(int)
        List of proportions in which nitrogenous bases occur ([3, 2 ,2, 3] as defalut to human as stated on wikipedia)'''

    # First we transform our proportions to fractions of 10 and sum it up so we have a renge 
    a_proportion = proportions[0]/10
    g_proportion = a_proportion + proportions[1]/10
    t_proportion = g_proportion + proportions[2]/10

    # Then we generate our sequence by takieng randomly generated number and comparing it to our range
    seq = ""
    for i in range(size):
        value = random()
        if value <= a_proportion:
            seq = seq + 'A'
 
        elif a_proportion < value <= g_proportion:
            seq = seq + 'G'

        elif g_proportion < value <= t_proportion:
            seq = seq + 'T'
        
        else:
            seq = seq + 'C'
    
    return seq

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TESTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
for j in range(1000):
    test_seq = generate_random_sequence(10)
    for i in test_seq:
        assert i == 'A' or i == 'T' or i == 'G' or i == 'C'