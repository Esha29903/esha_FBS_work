def area_of_circle(radius):
    area= 3.14*radius*radius
    return area
radius=int(input("enter radius:"))
area=area_of_circle(radius)
print(f'area of circle is:{area}')