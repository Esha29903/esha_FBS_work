class Vehicle:
    def __init__(self,person):
        self.person=person
    def calculate_toll(self):
        return 0

class Twowheeler(Vehicle):
    def calculate_toll(self):
        toll=20
        if self.person>2:
            toll+=10
            return toll
        
class Threewheeler(Vehicle):
    def calculate_toll(self):
        toll=30
        if self.person>3:
            toll+=20
            return toll 

class Fourwheeler(Vehicle):
    def calculate_toll(self):
        toll=40
        if self.person>4:
            toll+=40
            return toll  

class Heavyvehicle(Vehicle):
    def calculate_toll(self):
        toll=60
        if self.person>6:
            toll+=100
            return toll 

while True:
    print('''please select choice from below:
    1.Twowheeler
    2.Threewheeler
    3.Fourwheeler
    4.Heavyvehicle
    5.Exit ''')  
    ch= (input("enter your choice:"))
    if ch=='1':
        person=int(input('enter no of person:'))
        Vehicle=Twowheeler(person)
        print(f"total toll amount:{Vehicle.calculate_toll()}")

    elif ch=='2':
        person=int(input('enter no of person:'))
        Vehicle=Threewheeler(person)
        print(f"total toll amount:{Vehicle.calculate_toll()}" )   

    elif ch=='3':
        person=int(input('enter no of person:'))
        Vehicle=Fourwheeler(person)
        print(f"total toll amount:{Vehicle.calculate_toll()}")

    elif ch=='4':
        person=int(input('enter no of person:'))
        Vehicle=Heavyvehicle(person)
        print(f"total toll amount:{Vehicle.calculate_toll()}")

    elif ch=='5':
        print("exit")
        break 
    else:
        print("invalid choice")


        

    