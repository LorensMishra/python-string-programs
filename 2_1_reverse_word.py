class ReverseWords:
    def reverse_words(self, sentence):
        words = sentence.split()
    
        return words[::-1]


# Runtime input
obj = ReverseWords()
s = input("Enter a sentence: ")

print("Reversed Words:", obj.reverse_words(s))
