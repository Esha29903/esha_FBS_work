side1=int(input("Enter the side1 of a traingle: "))
side2=int(input("Enter the side2 of a triangle: "))
side3=int(input("Enter the side3 of a traingle: "))
if(side1+side2>side3 and side1+side3>side2 and side2+side3>side1):
    print(f'is a trinagle')
else:
    print(f'not a tringle')