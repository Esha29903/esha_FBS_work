id=input("enter your id:")
PASS=int(input("enter your PASS:"))
if (id=="admin" and PASS==1234):
    print("welcome admin")
else:
    print("invalid id or password")