#This program will find the area of a circle with the help of radius

print("<---------------AREA-OF-CIRCLE----------------->")

import math

radius = int(input("Enter the Radius of the Circle you want to find the Area of: "))
unit = input("Enter the Unit of the Radius(either cm,mm,m): ")

if unit == "m" or "cm" or "mm":
    print("Working on it,please wait... ")
else:
    print(f"{unit} is not a valid unit or is yet to be implemented.")


area = round((2*math.pi*radius**2),2) 

print(f"The Area of the Circle should be: {area} {unit}^2 ") 