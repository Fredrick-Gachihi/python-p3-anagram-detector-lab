# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        sorted_word = sorted(self.word)
        matches = []
        for w in word_list:
            sorted_w = sorted(w.lower())
            if sorted_word == sorted_w and self.word != w.lower():
                matches.append(w)

        return matches