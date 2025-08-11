subject1=int(input("enter subject 1 marks:"))
subject2=int(input("enter subject 2 marks:"))
subject3=int(input("enter subject 3 marks:"))
subject4=int(input("enter subject 4 marks:"))
subject5=int(input("enter subject 5 marks:"))
total_marks=subject1+subject2+subject3+subject4+subject5
average_marks=total_marks/5
if average_marks >= 90:
    print(f'firstclass:{average_marks}')
elif average_marks >= 80:
    print(f'secondclass:{average_marks}')
elif average_marks >= 70:
    print(f'thirdclass:{average_marks}')
elif average_marks >= 60:
    print(f'pass:{average_marks}')
else:    
    print(f'fail:{average_marks}')
