class Shirt:
    def __init__(self, id, name,type, price, size):
        self.sid = id
        self.sname = name
        self.stype = type
        self.sprice = price
        self.ssize = size

    def display(self):
        print("shirt id", self.sid)
        print("shirt name", self.sname)
        print("shirt type", self.stype)
        print("shirt price", self.sprice)
        print("shirt size", self.ssize)

    def __del__(self):
        pass
s1 = Shirt(0,"linen","formal",1200,"large")
s2 = Shirt(12,"peter england","casual",500,"medium")
s1.display()
print("#############################")
s2.display()        