##armstrongno
def armstrong(num, power_val):
    if num == 0:
        return 0
    return (num % 10) ** power_val + armstrong(num // 10, power_val)
n = int(input("Enter a number: "))
digits = len(str(n))

if armstrong(n, digits) == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")