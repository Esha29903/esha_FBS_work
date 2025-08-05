num=int(input("enter a three digit number:"))
temp=num

d1=temp%10
temp=temp//10
d2=temp%10
temp=temp//10
d3=temp%10
temp=temp//10
if(d3==2*d2 and d3==0.5*d1):
    print('yes you have done it.')
else:
    print("please try next time.")    

