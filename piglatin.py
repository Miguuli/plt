
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        words = self.phrase.split()
        translated_words = []
        for word in words:
            if '-' in word:
                subwords = word.split('-')
                translated_subwords = []
                for subword in subwords:
                    translated_subwords.append(self.translate_word(subword))
                translated_words.append('-'.join(translated_subwords))
            else:
                translated_words.append(self.translate_word(word))
        return " ".join(translated_words)

    def translate_word(self, word):
        # Handle punctuation
        punctuation = ''
        if not word[-1].isalpha():
            punctuation = word[-1]
            word = word[:-1]

        if word.endswith("y"):
            return word + "nay" + punctuation
        elif word[-1] in "aeiou" and not self.phrase[0] in "bcdfghjklmnpqrstwxz":
            return word + "yay" + punctuation
        else:
            first_vowel_index = next((i for i, char in enumerate(word) if char in "aeiou"), None)
            if first_vowel_index is not None and first_vowel_index > 0:
                return word[first_vowel_index:] + word[:first_vowel_index] + "ay" + punctuation
            else:
                return word + "ay" + punctuation

