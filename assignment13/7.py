# Program to remove a given key from dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
key = 'b'

if key in my_dict:
    del my_dict[key]

print("Dictionary after removal:", my_dict)