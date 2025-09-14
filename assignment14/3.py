# Program to find unique words and count frequency
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

unique_words = set(words)
print("Unique words:", unique_words)

for word in unique_words:
    print(f"{word}: {words.count(word)}")