num=int(input("enter three digit number"))
temp=num
d1=temp%10
temp=temp//10
d2=temp%10
temp=temp//10
d3=temp%10
temp=temp//10
sum=d1+d2+d3
print(f'add three digit no:{sum}.')
