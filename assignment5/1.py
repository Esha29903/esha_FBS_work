correct_id = "admin"
correct_pass = 1234
for attempt in range(3):
    id = input("Enter your ID: ")
    PASS = int(input("Enter your PASS: "))

    if id == correct_id and PASS == correct_pass:
        print("Welcome admin")
        break
    else:
        print("Invalid ID or password")
else:
    print( "Program terminated.")