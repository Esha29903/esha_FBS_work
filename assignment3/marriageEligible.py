gender=input("enter gender(M/F):")
age=int(input("enter age:"))

if((gender=="M" and age>=21) or (gender=="F" and age>=18)):
    print("eligible for marriage")
else:
    print("not eligible for marriage")
