angle1=int(input("enter a angle of triangle 1:"))
angle2=int(input("enter a angle of triangle 2:"))
angle3=int(input("enter a angle of triangle 3:"))

if(angle1>0 and angle2>0 and angle3>0 and (angle1+angle2+angle3)==180):
    print(f'is a triangle')
else:
    print(f'is not a traingle')