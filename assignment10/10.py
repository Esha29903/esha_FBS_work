numbers = [1, 2, 3, 2, 4, 2, 5, 2]
element = 2
result = [x for x in numbers if x != element]
print("Original List :", numbers)
print("Element to remove :", element)
print("Updated List :", result)