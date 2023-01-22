import string


# source_text = '/Users/palomavaldez-marsh/code/ACS-1120-Intro-Data-Structures/Code/test-text.txt'
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
        print(key, ":", histogram[key])

    return histogram

def unique_words(histogram):
    """
    description: function that that counts unique words in the histogram
    parameters: histogram
    returns: total count of unique words in the histogram
    """

    total_unique_words = len(histogram)
    print('-------------------------------------------------------------')
    print(f'The histogram contains {total_unique_words} unique words.')
    return total_unique_words


def frequency(word, histogram):
    """
    description: function that tells you how many times a word appears in a histogram
    parameters: word, histogram
    returns: total count of times a word appears in a text
    """
    word_appearances = histogram[word]
    print(f'The word {word} appears in the histogram {word_appearances} times.')
    return word_appearances

#  -----------------------------------------------------------------
    
if __name__ == '__main__':
    build_histogram('test-text.txt')
    unique_words(histogram)
    frequency('rabbit', histogram)
