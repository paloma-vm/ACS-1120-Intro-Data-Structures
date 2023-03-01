import random
import sys
import string

# class Sentence():
# sentence = ''
# filename = 'short-dictionary.txt'
# filename = '/usr/share/dict/words'
# number_of_words = int(sys.argv[1])
# number_of_words = 6

# random_words = []
# read in the words file
def read_words(filename, number_of_words): #this only works for a list of words, not source text
    # use make_sentence or file_to_words instead
    """
    A function to read the text file of words, 
    select a random set of words and store in a data type, 
    put the words into a "sentence", and output the sentence
    """
    infile = open(filename, "r")

    # words_list = infile.readlines()#reads whole dictionary
    words_list = [line.rstrip() for line in infile]

    infile.close

    random_words = random.sample(words_list, k=number_of_words)
    print("********************")
    print(random_words)
    print("----------------")

    for i in range(len(random_words[:-1])):
        print(random_words[i], end=" ")

    sentence = print(str(random_words[-1]) + ".") #puts the period in the correct place at end of sentence

    return sentence

def make_sentence(filename, number_of_words):
    """
    A function to read the text file of words, 
    select a random set of words and store in a data type, 
    put the words into a "sentence", and output the sentence
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

    random_words = random.sample(words_list, k=number_of_words)
    print("********************")
    print(random_words)
    print("----------------")

    sentence = " ".join(random_words) + "."
        
    print('########################')
    print(sentence)
    return sentence
    
    
if __name__ == '__main__':
    make_sentence('/usr/share/dict/words', 6)
    