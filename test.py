#simple interest
p=int(input("enter the principal amount:"))
r=int(input("enter the rate:"))
t=int(input("enter the time:"))
SI=(p*r*t)/100
print(f'simple interest:{SI}.')


##area and perimeter
l=int(input("enter the number l:"))
b=int(input("enter the number b:"))
r=int(input("enter the number r:"))
area=l*b
perimeter=2*(l+b)
print(f'area:{area},perimeter:{perimeter}.')


##convert km to m and cm
km=int(input("enter the no of km:"))
m=km*1000
cm=km*100000
print(f'KM:{km},M:{m},CM:{cm}.')