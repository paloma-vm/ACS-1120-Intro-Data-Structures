import sys
import string

def file_to_words(filename):
    """
    A function to read the source text, 
    and clean the file
    """
    words_list = []
    infile = open(filename, "r")

    lines = infile.readlines() # reads whole file
    for line in lines:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))

        words_in_line = line.split(" ")

        words_list.extend(words_in_line)

    infile.close

    return words_list