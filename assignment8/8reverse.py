def reverse_number(n):
    temp=n
    d1=temp%10
    temp=temp//10
    d2=temp%10
    temp=temp//10
    d3=temp%10
    temp=temp//10
    reverse_num=d1*100+d2*10+d3
    return reverse_num
n=int(input("enter three digit number :"))
reverse=reverse_number(n)
print(f'after reversing:{n} it becomes {reverse}.')