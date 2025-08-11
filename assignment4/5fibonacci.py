num=int(input('enter a number:'))
a=0
b=1
for i in range(num):
    c=a+b
    print(c)
    a=b
    b=c
