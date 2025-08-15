##fibonacci series
def fibonacci_series(n):
    a,b=0,1
    for i in  range(n):
        c=a+b
        print(c)
        a=b
        b=c
num=int(input('enter a number:'))
fibonacci_series(num)

    
