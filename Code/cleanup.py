# read in the words file and clean it up
def cleanup(filename):
    """
    A function to read the text file of words and clean it by 
        removing punctuation
    """
    infile = open(filename, "r")
    words_list = [line.rstrip() for line in infile]
    infile.close
    return words_list

if __name__ == "__main__":
    cleanup(filename)