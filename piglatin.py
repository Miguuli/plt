
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
            if word.endswith("y"):
                translated_words.append(word + "nay")
            elif word[-1] in "aeiou" and not self.phrase[0] in "bcdfghjklmnpqrstwxz":
                translated_words.append(word + "yay")
            else:
                first_vowel_index = next((i for i, char in enumerate(word) if char in "aeiou"), None)
                if first_vowel_index is not None and first_vowel_index > 0:
                    translated_words.append(word[first_vowel_index:] + word[:first_vowel_index] + "ay")
                else:
                    translated_words.append(word + "ay")
        return " ".join(translated_words)

