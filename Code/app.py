"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
import random
import sys
import sentence


app = Flask(__name__)

# filename = '/usr/share/dict/words'
# number_of_words = int(sys.argv[1])
# random_words = []


# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    # filename = '/usr/share/dict/words'
    # number_of_words = int(sys.argv[1])
    # random_words = []
    generated_sentence = sentence.read_words('/usr/share/dict/words', 6)
    print(generated_sentence)
    return print(f"<p>{generated_sentence}</p>")
    
    return sentence.read_words('/usr/share/dict/words', 6)
    # context = {
    #     'filename': filename,
    #     'number_of_words': number_of_words,
    #     'random_words': random_words,
        # 'generated_sentence': generated_sentence
    # }

    # return render_template('index.html')

    # return render_template('index.html', **context)

    # return "<p>TODO: Return a word here!</p>"
    # return generated_sentence


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
