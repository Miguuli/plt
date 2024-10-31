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

    # if word ends with y, append nay to the end of the word
    # if word ends with vowel, append yay to the end of the word
    # if word ends with consonant, append ay to the end of the word
    def test_translate_any_equals_anynay(self):
        # Initialize a translator with a phrase
        translator = PigLatin("any")
        # Get the phrase
        phrase = translator.get_phrase()
        # Get the Pig Latin translation
        translation = translator.translate()
        self.assertEqual("anynay", translation, phrase)

    # if word ends with y, append nay to the end of the word
    # if word ends with vowel, append yay to the end of the word
    # if word ends with consonant, append ay to the end of the word
    def test_translate_apple_equals_appleyay(self):
        # Initialize a translator with a phrase
        translator = PigLatin("apple")
        # Get the phrase
        phrase = translator.get_phrase()
        # Get the Pig Latin translation
        translation = translator.translate()
        self.assertEqual("appleyay", translation, phrase)

    # if word ends with y, append nay to the end of the word
    # if word ends with vowel, append yay to the end of the word
    # if word ends with consonant, append ay to the end of the word
    def test_translate_ask_equals_askyay(self):
        # Initialize a translator with a phrase
        translator = PigLatin("ask")
        # Get the phrase
        phrase = translator.get_phrase()
        # Get the Pig Latin translation
        translation = translator.translate()
        self.assertEqual("askay", translation, phrase)

    # if word ends with y, append nay to the end of the word
    # if word ends with vowel, append yay to the end of the word
    # if word ends with consonant, append ay to the end of the word
    def test_translate_hello_equals_ellohay(self):
        # Initialize a translator with a phrase
        translator = PigLatin("hello")
        # Get the phrase
        phrase = translator.get_phrase()
        # Get the Pig Latin translation
        translation = translator.translate()
        self.assertEqual("ellohay", translation, phrase)


    # if word ends with y, append nay to the end of the word
    # if word ends with vowel, append yay to the end of the word
    # if word ends with consonant, append ay to the end of the word
    def test_translate_known_equals_ownknay(self):
        # Initialize a translator with a phrase
        translator = PigLatin("known")
        # Get the phrase
        phrase = translator.get_phrase()
        # Get the Pig Latin translation
        translation = translator.translate()
        self.assertEqual("ownknay", translation, phrase)

    # if word ends with y, append nay to the end of the word
    # if word ends with vowel, append yay to the end of the word
    # if word ends with consonant, append ay to the end of the word
    def test_translate_hello_world_ellohay_orldway(self):
        # Initialize a translator with a phrase
        translator = PigLatin("hello world")
        # Get the phrase
        phrase = translator.get_phrase()
        # Get the Pig Latin translation
        translation = translator.translate()
        self.assertEqual("ellohay orldway", translation, phrase)

    # if word ends with y, append nay to the end of the word
    # if word ends with vowel, append yay to the end of the word
    # if word ends with consonant, append ay to the end of the word
    # test for translating well-being to ellway-eingbay
    def test_translate_well_being(self):
        # Initialize a translator with a phrase
        translator = PigLatin("well-being")
        # Get the phrase
        phrase = translator.get_phrase()
        # Get the Pig Latin translation
        translation = translator.translate()
        self.assertEqual("ellway-eingbay", translation, phrase)

    # if word ends with y, append nay to the end of the word
    # if word ends with vowel, append yay to the end of the word
    # if word ends with consonant, append ay to the end of the word
    # test for translating hello world! to ellohay orldway!
    def test_translate_hello_world_with_punctuation(self):
        # Initialize a translator with a phrase
        translator = PigLatin("hello world!")
        # Get the phrase
        phrase = translator.get_phrase()
        # Get the Pig Latin translation
        translation = translator.translate()
        self.assertEqual("ellohay orldway!", translation, phrase)

  # if word ends with y, append nay to the end of the word
    # if word ends with vowel, append yay to the end of the word
    # if word ends with consonant, append ay to the end of the word
    # test for translating uppercase APPLE to APPLEYAY
    def test_translate_APPLE(self):
        # Initialize a translator with a phrase
        translator = PigLatin("APPLE")
        # Get the phrase
        phrase = translator.get_phrase()
        # Get the Pig Latin translation
        translation = translator.translate()
        self.assertEqual("APPLEYAY", translation, phrase)
