from dictogram import Dictogram
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
class DictogramTest(unittest.TestCase):

    # Test fixtures: known inputs and their expected results
    fish_words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    fish_list = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
    fish_dict = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}

    def test_sample(self):
        histogram = Dictogram(self.fish_words)
        # Create a list of 10,000 word samples from histogram
        samples_list = [histogram.sample() for _ in range(10000)]
        # Create a histogram to count frequency of each word
        samples_hist = Dictogram(samples_list)
        # Check each word in original histogram
        for word, count in histogram.items():
            # Calculate word's observed frequency
            observed_freq = count / histogram.tokens
            # Calculate word's sampled frequency
            samples = samples_hist.frequency(word)
            sampled_freq = samples / samples_hist.tokens
            # Verify word's sampled frequency is close to observed frequency
            lower_bound = observed_freq * 0.9  # 10% below = 90% = 0.9
            upper_bound = observed_freq * 1.1  # 10% above = 110% = 1.1
            assert lower_bound <= sampled_freq <= upper_bound


if __name__ == '__main__':
    unittest.main()
