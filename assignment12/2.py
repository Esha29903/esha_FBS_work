s = input("Enter a string: ")
n = int(input("Enter index to remove: "))
new_s = s[:n] + s[n+1:]
print("String after removal:", new_s)