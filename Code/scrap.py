import random
import sys

filename = 'short-dictionary.txt'
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
    
    for word in random_words.range(number_of_words - 1): 
        print(word, end=" ")

    # print(display_sentence)
    print("********************")
    print(random_words)
    print("\b")
    print(".\n")
    

# def print_sentence():
#     print("----------------")
#     print(random_words)
#     for word in random_words:
#         print(word, end=' ')
#     print(".\n")
    
if __name__ == '__main__':
    read_words()
    
