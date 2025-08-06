P=int(input("enter  principal:"))
T=int(input("enter  time:"))
R=int(input("enter  rate:"))
CI=P*((1+R/100)**T)-P
print(f'compound interest:{CI}')