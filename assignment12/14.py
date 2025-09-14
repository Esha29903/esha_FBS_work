s = input("Enter a string: ")
words = s.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Occurrences of each word:")
for k, v in freq.items():
    print(k, ":", v)