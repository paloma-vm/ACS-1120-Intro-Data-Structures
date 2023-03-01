"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
import random
import sys
from sentence import make_sentence
import cleanup
import pprint
from file_to_words import file_to_words
from nth_markov import MarkovChain



app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.






# Before Markov
# -------------------------------------------------------------
# @app.route("/")
# def home():
#     """Route that returns a web page containing the generated text."""
#     filename = 'test-text.txt'
#     number_of_words = 6
#     # random_words = []
#     generated_sentence = make_sentence(filename, number_of_words)
#     print('____________________________________')
#     # print(generated_sentence)
#     return f"<p>{generated_sentence}</p>"
#     # return f"<p>m</p>"


# Using Markov
# -------------------------------------------------------------
@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    corpus = file_to_words('text_files/peas.txt')
    markov_chain = MarkovChain(corpus=corpus, order=2)
    generated_sentence = markov_chain.random_walk(9)
    return generated_sentence


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)

    
