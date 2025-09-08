# Program to generate dictionary (x, x*x) from 1 to n
n = 5
squares_dict = {x: x*x for x in range(1, n+1)}

print("Generated Dictionary:", squares_dict)