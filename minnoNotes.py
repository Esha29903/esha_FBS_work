amt=int(input("enter amount to calculate min no. of notes:"))
temp=amt

two_thousand=temp//2000
temp=temp%2000

five_hundered=temp//500
temp=temp%500

two_hundered=temp//200
temp=temp%200

fifty=temp//50
temp=temp%50

twenty=temp//20
temp=temp%20

ten=temp//10
temp=temp%10

min_notes=two_thousand+five_hundered+two_hundered+fifty+twenty+ten
print(f'min no of notes:{min_notes}.')


