total_marks = 0
for i in range(1, 6):
    marks = int(input(f"Enter subject {i} marks: "))
    total_marks += marks

average_marks = total_marks / 5
print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks}")