
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        if self.phrase.endswith("y"):
            return self.phrase + "nay"
        elif self.phrase[-1] in "aeiou" and not self.phrase[0] in "bcdfghjklmnpqrstwxz":
            return self.phrase + "yay"
        elif self.phrase[-1] in "aeiou" and self.phrase[0] in "bcdfghjklmnpqrstwxz":
            return self.phrase.replace(self.phrase[0], "") + "hay"
        else:
            first_vowel_index = next((i for i, char in enumerate(self.phrase) if char in "aeiou"), None)
            if first_vowel_index is not None and first_vowel_index > 0:
                return self.phrase[first_vowel_index:] + self.phrase[:first_vowel_index] + "ay"
            return self.phrase + "ay"

