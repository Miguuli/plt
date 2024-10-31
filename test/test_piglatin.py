import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        # Initialize a translator with a phrase
        translator = PigLatin("hello world")
        # Get the phrase
        phrase = translator.get_phrase()
        self.assertEqual("hello world", phrase)