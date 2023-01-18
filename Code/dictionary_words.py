import random
import sys

# filename = 'short-dictionary.txt'
filename = '/usr/share/dict/words'
number_of_words = int(sys.argv[1])
random_words = []
# read in the words file
def read_words():
    """
    A function to read the text file of words, 
    select a random set of words and store in a data type, 
    put the words into a "sentence", and output the sentence
    """
    infile = open(filename, "r")

    words_list = infile.readlines()#reads whole dictionary

    infile.close

    random_words = random.sample(words_list, k=number_of_words)
    print("********************")
    print(random_words)
    print("----------------")
    
    for word in random_words:
        word = word.strip()
   
        print(word, end=" ")

    print(".\n")

# still need to move the period back one space, I'm not sure how
    
if __name__ == '__main__':
    read_words()
