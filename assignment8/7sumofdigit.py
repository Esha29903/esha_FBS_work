def sum_of_digits(n):
    temp=n
    sum=0
    while(temp>0):
        d=temp%10
        print(d)
        temp=temp//10
        sum=sum+d
    print(f'sum of digit is:{sum}')
num=int(input('enter a no:'))
sum_of_digits(num)