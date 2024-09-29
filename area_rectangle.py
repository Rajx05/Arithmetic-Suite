#Project Area of a Rectangle
#here we will learn how to make find area of a rectangle

print("<---------------AREA-OF-RECTANGLE------------------>")

l = float(input("Enter Lenght of the Rectangle:"))
b = float(input("Enter the Breadth of the Rectangle:"))
unit = input("Enter the Unit the lenght and breadth of the Rectangle are in(either cm,mm,m,etc): ")

area = l*b 

print(f"The Area of the Rectangle should be : {area} {unit}^2")
