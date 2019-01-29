import unittest


class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word
        # string = input_string.split(" ")
        # punctuation = "?!:,"

        self.words_to_counts = {}
        # for word in string:
        #     word = word.strip(punctuation)
        #     if word == "-":
        #         continue
            
        #     if word.lower() not in self.words_to_counts:
        #         self.words_to_counts[word.lower()] = 0
        #     self.words_to_counts[word.lower()] += 1
        
        start_idx = 0
        i=0 # current index
        words = []
        for char in input_string:
            if not char.isalpha():
                words.append(input_string[start_idx:i])
                start_idx = i+1
            i+=1
        
        for word in words:
            if word.lower() not in self.words_to_counts: 
                self.words_to_counts[word.lower()] = 0
            self.words_to_counts[word.lower()] += 1

        # find the words - loop through keep track of start index and 


# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'i': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'strawberry': 1, 'short': 1, 'yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"bakery": 1, "cakes": 1, "allie's": 1, "sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)