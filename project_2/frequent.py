from counting_patterns import pattern_count

def frequent_words(seq, pattern_length):
    '''Function which returns set of the most frequently occuring patterns
    Parameters:
    ----------
    seq : str
        DNA sequence in which we are looking for patterns
    
    pattern_length : int
        Lenght of patterns we are looking for'''

    frequent_patterns = set()
    # Here we count each pattern of given length
    # Patterns and their occurences are stored in different lists at their consequent positions
    counts = [0] * (len(seq) - pattern_length)
    for i in range(len(seq) - pattern_length):
        pattern = seq[i: i+pattern_length]
        counts[i] = pattern_count(seq, pattern)

    maxCount = max(counts)
    # Here we add the most frequent patterns to our set
    for i in range(len(seq) - pattern_length):
        if counts[i] == maxCount:
            frequent_patterns.add(seq[i: i+pattern_length])

    return frequent_patterns

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TESTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
if __name__ == '__main__':
    example = 'ATCATGATAATT'
    pattern_length = 2
    assert frequent_words(example, pattern_length) == {'AT'}
