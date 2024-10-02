
#This is the Intergrated Version of Arithmetic Suite.
#this is also used to make the exe.

print("<---------------------ARITHMETIC-SUITE------------------------->")

print("What would you like to do? ")
print("Enter 1 for Finding Area of Triangle.")
print("Enter 2 for Finding Area of Rectangle.")
print("Enter 3 for Using Calculator")
print("Enter 4 for Finding Area of Circle.")
print("Enter 5 for Using Arithmetic Progression Tools.")

command = input("Enter Desired Mode of operation: ")

if command == "1":
    print("<--------------AREA-OF-TRIANGLE----------------->")    #Area of Triangle Module(area_triangle)

    h = float(input("Enter the Height of the Triangle: "))
    b = float(input("Enter the Lenght of Base of the Triangle: "))
    unit = input("Enter the Unit of measurement(either cm,mm,m,etc): ")
    
    area = (1/2*b*h)
   
    print(f"THE AREA FOR THE TRIANGLE SHOULD BE: {area} {unit}^2")
    input("Press 'Enter' to exit..")

elif command == "2":
    print("<---------------AREA-OF-RECTANGLE------------------>")   #Area of Rectangle Module(area_rectangle)

    l = float(input("Enter Lenght of the Rectangle:"))
    b = float(input("Enter the Breadth of the Rectangle:"))
    unit = input("Enter the Unit the lenght and breadth of the Rectangle are in(either cm,mm,m,etc): ")

    area = l*b 

    print(f"The Area of the Rectangle should be : {area} {unit}^2")
    input("Press 'Enter' to exit...")

elif command == "3":
    
    print("<---------------CALCULATOR----------------->")   #Simple Python calc(py_calc)
    
    print("Enter '+' for Addition")
    print("Enter '-' for Subtraction")   
    print("Enter '/' for Division")
    print("Enter '*' for Multiplication")

    operator = input("entrator either '+ - * /': ")

    num1 = int(input("Enter Number one: "))
    num2 = int(input("Enter Second one: "))

    if operator == "+":
       result = num1 + num2
       print(f"The correct Answer should be: {result}")
       input("Press 'Enter' to exit...")
    elif operator == "-":
        result = num1 - num2
        print(f"The Correct Answer should be: {result}")
        input("Press 'Enter' to exit...")
    elif operator == "/":
        result = num1 / num2
        print(f"The Correct Answer should be: {result}")
        input("Press 'Enter' to exit...")
    elif operator == "*":
        result = num1 *num2
        print(f"The correct Answer should be: {result}")
        input("Press 'Enter' to exit...")
    else:
        print("You have NOT entered any operator")
        input("Press 'Enter' to exit...")

elif command == "4":

    print("<---------------AREA-OF-CIRCLE----------------->")       #Area if Circle Module(area_circle)

    import math

    radius = int(input("Enter the Radius of the Circle you want to find the Area of: "))
    unit = input("Enter the Unit of the Radius(either cm,mm,m): ")

    if unit == "m" or "cm" or "mm":
        print("Working on it,please wait... ")
    else:
        print(f"{unit} is not a valid unit or is yet to be implemented.")
        input("Press 'Enter' to exist")

    area = round((2*math.pi*radius**2),2) 

    print(f"The Area of the Circle should be: {area} {unit}^2 ")
    input("Press 'Enter' to exit...")

elif command == "5":
    
    print("<---------------ARITHMETIC-PROGRESSION----------------->")  #Arithmetic Progression(ap)
    print("What would you like to find?")
    print("Enter 1 for Finding nTH Term of AP")
    print("Enter 2 for Finding Sum of AP to nTh term")

    command =  input("Enter Which Ever Operation You Would Like To Perform: ")
    
    if command == "1":
        print("<-------------FINDING-THE-NTH-TERM---------------->") #Finding the nTH term of AP(ap_nth_term)

        a = float(input("Enter the a of FIRST term of the AP: "))
        n = float(input("Enter the nTH term you want to find: "))
        d = float(input("Enter Common Difference of AP: "))

        nth_term = (a+(n-1)*d)

        print(f"The nTH term of AP is: {nth_term}")
        input("Press 'Enter' to exit...")

    elif command == "2":
        print("<------------SUM-TILL-NTH-TERM-------------->")  #Finding Sum till nTH term of AP(ap_sum_nth_term)

        a = float(input("Enter the FIRST Term of AP: "))
        d = float(input("Enter the COMMON DIFFERENCE of AP: "))
        n = float(input("Enter the nTH term you want to find the sum till: "))

        s = (n/2) * (2 * a + (n - 1) *d)

        print(f"The sum till the {n}th term should be: {s}")
        input("Press 'Enter' to exit...")

else:
    print("The Type of operator you want is not available right now or is yet to be implemented.")
    input("Press 'Enter' to exit...")
