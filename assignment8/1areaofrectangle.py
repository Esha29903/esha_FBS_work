##area of rectangle
def area_of_rectangle(length,width):
    area=length*width
    return area
length=int(input("enter length:"))
width=int(input("enter width:"))
area=area_of_rectangle(length,width)
print(f"area of rectangle is {area}")
