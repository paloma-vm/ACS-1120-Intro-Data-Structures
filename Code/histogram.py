import random
import sys
import re
import string


source_text = '/Users/palomavaldez-marsh/code/ACS-1120-Intro-Data-Structures/Code/test-text.txt'
# dictionary of 'word' : count
histogram = {}

# read in the words file
def build_histogram(source_text):
    """
    description: takes the contents of a text file and returns a dictionary 
    parameters: source_text
    returns: dictionary of key:value pairs
    """
    infile = open(source_text, "r")

    lines = infile.readlines()#reads whole file
    print(lines)
    # loop through lines in text file
    for line in lines:
        # remove newlines and leading spaces
        line = line.strip()
        # convert to lowercase so everything is uniform
        line = line.lower()
        # remove all punctuation by translating all chars to unicode and mapping them 
        # string.punctuation gives all the sets of puntuation (import string to use)
        line = line.translate(line.maketrans("", "", string.punctuation))
        # ^ help from https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file/?ref=gcse

        # splits the line into words
        words_in_line = line.split(" ")

        for word in words_in_line:
            if word in histogram: # check to see if word is in dictionary
                histogram[word] = histogram[word] + 1
            else:
                histogram[word] = 1


    infile.close

    # print the histogram dictionary
    for key in list(histogram.keys()):
        print(key, " ", histogram[key])

    # random_words = random.sample(words_list, k=number_of_words)
    # print("********************")
    # print(words_list)
    # print("----------------")

def unique_words():
    """
    description: function that that counts unique words in the histogram
    parameters: histogram
    returns: total count of unique words in the histogram
    """

def frequency():
    """
    description: function that t
    parameters: word, histogram
    returns: total count of times a word appears in a text
    """


#  -----------------------------------------------------------------
    
if __name__ == '__main__':
    build_histogram(source_text)
