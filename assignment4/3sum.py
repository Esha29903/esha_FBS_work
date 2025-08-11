n=int(input('enter a number:'))
temp=n
sum=0
while(temp>0):
    d=temp%10
    print(d)
    temp=temp//10
    sum=sum+d
    print(f'sum of digit is:{sum}')
