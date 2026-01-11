class ReverseWords:
    def reverse_words(self, sentence):
        words = sentence.split()
        words.reverse()
        return " ".join(words)


# Runtime input
obj = ReverseWords()
s = input("Enter a sentence: ")

print("Reversed Words:", obj.reverse_words(s))
