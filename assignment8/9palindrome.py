def is_palindrome(num):
    reverse_num= (num% 10) * 100 + ((num// 10) % 10) * 10 + (num// 100)
    if num == reverse_num:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
n=int(input("enter a three digit no:"))
is_palindrome(n)    