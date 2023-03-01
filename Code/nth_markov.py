
import random
from dictogram import Dictogram
import dictogram


MARKOV_START_TOKEN = 'markovstart'
MARKOV_END_TOKEN = 'markovend'

# nth order Markov Chain model

# dictionary that stores windows as the key in the key-value pair
# the value for each key is a dictogram

class MarkovChain(dict):
    """ nth order Markov Chain class""" 
    #using Dani's code from Grain video to try to move forward with tweet generator in interest of time
    def __init__(self, corpus, order=2):
        self.corpus = corpus
        self.order = order
        self.markov_dict = dict()


        # build the chain once
        tuples = []
        window = []

        for i in range (len(self.corpus) - self.order): # iterate over corpus, 2 for 2nd order
            for n in range(self.order): # iterate over the order to generate word windows
                window.append(self.corpus[i + n]) #create word windows
                tuples.append((tuple(window), self.corpus[i + self.order])) # store the windows in a list of tuples
                window = [] # re-create the window every time you iterate over the order
   
        # Add the tuples to the dict, iterate over the tuples
        for window in tuples:
            if window[0] in self.markov_dict:
                self.markov_dict[window[0]].add_count(window[1])
            else:
                self.markov_dict[window[0]] = dictogram.Dictogram([window[1]])

     # walk the chain many times 
    def random_walk(self, distance=None):
        # Walk along the instance of the Markov Chain to make a new sentence.
        steps = 0
        output = []
        window = (MARKOV_START_TOKEN,)
        walking = True

        while walking:
            word = dictogram.Dictogram.sample(self.markov_dict[window])
            window = list(window[1:])
            window.append(word)
            window = tuple(window)
            walking = (distance is not None and steps <= distance) and (word != MARKOV_END_TOKEN)
            if walking:
                steps += 1
                output.append(word)
        
        return ' '.join(output)

if __name__ == '__main__':
    import pprint
    from file_to_words import file_to_words

    corpus = file_to_words('text_files/peas.txt')
    markov_chain = MarkovChain(corpus=corpus, order=2)
    pprint.pprint(markov_chain.markov_dict)
    pprint.pprint(markov_chain.random_walk(9))


