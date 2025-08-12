num_passengers = int(input("Enter number of passengers: "))
ticket_price = float(input("Enter ticket price: "))
total_amount = 0

for i in range(1, num_passengers + 1):
    age = int(input(f"Enter age of passenger {i}: "))
    if age < 12:
        amt = ticket_price * 0.7  
    elif age > 59:
        amt = ticket_price * 0.5  
    else:
        amt = ticket_price        
    total_amount += amt

print(f'total amount of ticket to travel is:{total_amount}')