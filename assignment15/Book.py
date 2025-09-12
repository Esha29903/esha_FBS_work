class Book:
    def __init__(self, id, name, price,author):
        self.bid = id
        self.bname = name
        self.bprice = price
        self.bauthor = author

    def showBook(self):
        print("book id", self.id)
        print("book name", self.name)
        print("book price", self.price)
        print("book author", self.author)

    def __del__(self):
        pass
b1= Book(101,"python Programming",500,"Guido")
b2 = Book(201,"two states",500,"Chetan bhagat")
b1.showBook()
print("#############################")
b2.showBook()