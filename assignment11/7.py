list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("List1:", list1)
print("List2:", list2)

intersection_list = []
for i in list1:
    if i in list2 and i not in intersection_list:
        intersection_list.append(i)
print("Intersection of two lists:", intersection_list)