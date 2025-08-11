number = int(input("Enter a three digit number: "))
reverse_number = (number % 10) * 100 + ((number // 10) % 10) * 10 + (number // 100)
if number == reverse_number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")