def pattern_count(seq, pattern):
    '''Function which returns the number of how many times given pattern occured in given sentence
    Parameters:
    ----------
    seq : str
        DNA sequence in which we are looking for patterns
    
    pattern : str
        Pattern we are counting
    '''
    # We simply count each occurence of pattern in sequence
    count = 0
    for i in range(len(seq) - len(pattern)):
        if seq[i: i+len(pattern)] == pattern:
            count += 1

    return count


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TESTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
if __name__ == '__main__':
    test_seq = 'ATCATGATAATT'
    test_pattern = 'AT'
    assert pattern_count(test_seq, test_pattern) == [0, 3, 6, 9]
