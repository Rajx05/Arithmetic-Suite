#We will find the area of triangle.

print("<--------------AREA-OF-TRIANGLE----------------->")

h = float(input("Enter the Height of the Triangle: "))
b = float(input("Enter the Lenght of Base of the Triangle: "))
unit = input("Enter the Unit of measurement(either cm,mm,m,etc): ")
    
area = (1/2*b*h)
if unit == "cm" or "mm" or "m":
   print(f"THE AREA FOR THE TRIANGLE SHOULD BE: {area} {unit}^2")