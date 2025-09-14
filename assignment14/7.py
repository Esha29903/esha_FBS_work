# Program to find missing numbers in each set
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6, 7}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Missing in set2 compared to set1:", missing_in_set2)
print("Missing in set1 compared to set2:", missing_in_set1)