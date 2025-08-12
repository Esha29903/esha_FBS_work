start = int(input("Enter start amount: "))
end = int(input("Enter end amount: "))

notes = [2000, 500, 200, 50, 20, 10]

for amt in range(start, end + 1):
    temp = amt
    min_notes = 0
    for note in notes:
        count = temp // note
        min_notes += count
        temp = temp % note
    print(f"Amount: {amt}, Minimum notes: {min_notes}")