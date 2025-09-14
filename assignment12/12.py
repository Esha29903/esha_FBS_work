s = input("Enter a string: ")
count = 0
for ch in s:
    if ch.islower():
        count += 1
print("Number of lowercase characters:", count)