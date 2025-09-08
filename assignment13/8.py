# Program to count frequency of words in a string using dictionary
text = "python is easy and python is powerful"

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequency:", freq)