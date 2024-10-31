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

    def test_translate_empty_phrase(self):
        # Initialize a translator with a phrase
        translator = PigLatin("")
        # Get the phrase
        phrase = translator.get_phrase()
        # Get the Pig Latin translation
        translation = translator.translate()
        self.assertEqual("nil", translation, phrase)
