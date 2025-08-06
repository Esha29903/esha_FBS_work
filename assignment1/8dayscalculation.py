days=int(input("Enter days:"))
years=days//365
days=days%365
week=days//7
days=days%7
print(f'{years}years {week}week {days}days.')