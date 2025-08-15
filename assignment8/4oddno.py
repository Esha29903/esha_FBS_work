def sum_odd(n):
    s = 0
    for i in range(1, n+1, 2):  # step 2 means only odd numbers
        s = s + i
    return s

n = int(input("Enter n: "))
print("Sum of odd numbers =", sum_odd(n))