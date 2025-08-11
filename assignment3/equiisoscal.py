a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a==b==c:
    print(f'the triangle is equilateral ')
elif a== b or b==c or c==a:
    print(f'the triangle is isoceles ')  
else:
    print(f'the triangle is scalene ')      
