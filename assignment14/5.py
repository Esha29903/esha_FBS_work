# Program to find longest common prefix
words = ["flower", "flow", "flight"]

prefix = ""
for i in range(len(min(words, key=len))):
    chars = set(word[i] for word in words)
    if len(chars) == 1:
        prefix += chars.pop()
    else:
        break

print("Longest Common Prefix:", prefix)