import random
import sys

# filename = 'short-dictionary.txt'
# filename = '/usr/share/dict/words'
number_of_words = int(sys.argv[1])
random_words = []
# read in the words file
def read_words(filename):
    """
    A function to read the text file of words, 
    select a random set of words and store in a data type, 
    put the words into a "sentence", and output the sentence
    """
    infile = open(filename, "r")

    # words_list = infile.readlines()#reads whole dictionary
    words_list = [line.rstrip() for line in infile] #reads whole dictionary and 
    # help from https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
    print(words_list)
    infile.close
    return words_list

def make_random_sentence(words_list, number_of_words):
    """
    description: function that takes a list of words and returns a random sentence
    parameters: words_list
    returns: sentence created with randomly selected words
    """

    random_words = random.sample(words_list, k=number_of_words)
    print("********************")
    print(random_words)
    print("----------------")

#  -----------------------------------------------------------------
    # for word in random_words:
    #     word = word.strip()
    # for i in range(len(random_words)):
    #     # random_words[i] = random_words[i].strip
    #     random_words[i].strip

   
    for i in range(len(random_words[:-1])):
        # random_words[i] = random_words[i].strip
        print(random_words[i], end=" ")
    # for i in range(random_words[-1]):

    random_sentence = str(random_words[-1]) + "." #puts the period in the correct place at end of sentence
    print(random_sentence)

    # print(str(random_words[-1]) + ".") #puts the period in the correct place at end of sentence

    
if __name__ == '__main__':
    read_words('fish.txt')
    make_random_sentence(words_list, 6
    )
