age1=int(input('enter age1:'))
age2=int(input('enter age2:'))
age3=int(input('enter age3:'))
age4=int(input('enter age4:'))
age5=int(input('enter age5:'))
ticket=int(input('enter ticket price:'))

#person1
if(age1<12):
    amt1=ticket*0.7
elif(age1>59):   
     amt1=ticket*0.5
else:
     amt1=ticket

#person2     
if(age2<12):
    amt2=ticket*0.7
elif(age2>59):   
     amt2=ticket*0.5
else:
     amt2=ticket

#person3  
if(age3<12):
    amt3=ticket*0.7
elif(age3>59):   
     amt3=ticket*0.5
else:
     amt3=ticket

#4 
if(age4<12):
    amt4=ticket*0.7
elif(age4>59):   
     amt4=ticket*0.5
else:
     amt4=ticket  

#5
if(age5<12):
    amt5=ticket*0.7
elif(age5>59):   
     amt5=ticket*0.5
else:
     amt5=ticket

total_amount=amt1+amt2+amt3+amt4+amt5
print(f'total amount of ticket to travel is:{total_amount}')