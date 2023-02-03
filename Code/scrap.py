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

# ------------------------------------------------
def find_expected_probability(histogram):
    """
    description: function that takes a histogram and returns the expected probabilities
    of each word being selected when the histogram is sampled
    parameters: histogram
    returns: probabilities of each word being in the sample
    """
   
    words = list(histogram.keys()) # convert dict_keys object to a list
    list_word_tokens = list(histogram.values()) # convert dict_values object to a list
    total_word_tokens = sum(list_word_tokens)
    print(total_word_tokens)
    dart = random.uniform(0, total_word_tokens) # dart on number line
    
    fence = 0
    for word, count in histogram:
        fence += count
        if fence >= dart:
            print(word)
            return word


    for i in range(len(list_word_tokens)):
        list_word_tokens[i] = list_word_tokens[i] / total_word_tokens
    expected_probability_dict = dict(zip(words, word_tokens))
        # ^ help from https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
    # print(words)
    # print(word_tokens)
    print(expected_probability_dict)
    # print(str(expected_probability_dict))

    # print the expected probability dictionary
    print('word    expected probability')
    for key in list(expected_probability_dict.keys()):
        print(key, "   :", expected_probability_dict[key])
    return expected_probability_dict
    
if __name__ == '__main__':
    read_words()
    
