# Program to remove intersection of set2 from set1
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6}

set1 -= set1 & set2
print("After removing intersection:", set1)