"""Find how often a token appears after another token"""

"""First, take corpus and divide into strings based on separation by spaces"""
corpus = 'fish.txt'
for word in list_of_words:

     def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        # help from Andrew 
        word_located = False
        new_dict = {}

        for i in list_of_words:
            if i== word:
                i[1] += count
                word_located = True
                break

        if not word_located:
            self.append([word, count])
            self.types += 1

        self.tokens += count

