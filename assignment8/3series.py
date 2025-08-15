##sum of series
def sum_series(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total 
n=int(input("enter no:"))
print("sum of series is:", sum_series(n))   
     
##2
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact    
def sum_fact_series(n):    
    total=0
    for i in range(1,n+1):
        total+=fact(i)
    return total
n = int(input("Enter no: "))
result=sum_fact_series(n)
print("sum of factorial series is:", result)


##3
def sum_of_power(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total
n = int(input("Enter no: "))
result= sum_of_power(n)
print("Sum of power series is:", result)