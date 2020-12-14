def read_fasta(file_path):
    ''' Function which returns the sequence from FASTA file in a list
    Parameters:
    ----------
    file_path : str
        PATH to the FASTA file user wants to read
    '''
    # Here we open the file in "read only" mode, read it line by line, and close the IO 
    try:
        file = open(file_path, 'r')
        sequence_lists = file.readlines()
        file.close()
    
    # Here we handle the exceptions
    except TypeError:
        print("Wrong type. Try using string format eg. \".\\\\file.txt\"")
    except FileNotFoundError:
        print("File not found. Try again.")

    # Here we deal with the unwanted first line
    sequence_lists.pop(0)
    
    # Here we create sequence string and join all the lines into one string
    sequence = ''
    for i in sequence_lists:
        sequence += i
    
    # Here we remove unwanted empty lines, spaces and we make sure that all chars are in upper case
    sequence = sequence.replace('\n', '').replace(' ', '').upper()

    # Here we return our sequence paresed to a list
    return sequence.split('\r\n')

assert (read_fasta('.\\Test_file.txt')) == ['AAAAAA']
