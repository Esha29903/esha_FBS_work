# Program to find unique triplets with given sum
numbers = [1, 2, -1, 0, -2, 1, -1]
target = 0

triplets = set()
n = len(numbers)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if numbers[i] + numbers[j] + numbers[k] == target:
                triplets.add(tuple(sorted((numbers[i], numbers[j], numbers[k]))))

print("Unique triplets with sum", target, ":", triplets)