##print first n prime no
n = int(input("Enter a no: "))
count = 0
num = 2
while count < n:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1
    num += 1

##2 sum of series
n=int(input('enter a number:'))
sum_fact = 0
for i in range(1, n+1):
    fact = 1
    for i in range(1, i+1):
        fact *= i
    sum_fact += fact
print("Sum of factorial series:", sum_fact)    



##basic salary
basic = int(input("Enter basic salary: "))
if basic < 20000:
    da = basic * 0.10
    ta = basic * 0.12
    hra = basic * 0.15
else:
    da = basic * 0.15
    ta = basic * 0.18
    hra = basic * 0.20

total_salary = basic + da + ta + hra

print("Total salary =", total_salary)


##4
rows = 5  
for i in range(rows):
    if i % 2 == 0:        
        print("10101")
    else:                 
        print("01010")