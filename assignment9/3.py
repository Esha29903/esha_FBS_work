def reverse_number(num, rev=0):
    if num == 0:
        return rev
    rev = rev * 10 + num % 10
    return reverse_number(num // 10, rev)
n = int(input("Enter a number: "))
print("Reversed Number:", reverse_number(n))