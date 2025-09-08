def SOD(n):
    if(n==0):
        return 0
    return(n%10) + (n//10)
    
num=int(input("enter a no:"))
print('sum of digit is',SOD(num))   