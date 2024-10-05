
#This is the Intergrated Version of Arithmetic Suite.
#this is also used to make the exe.
import math


print("<---------------------ARITHMETIC-SUITE------------------------->")

print("What would you like to do? ")
print("Enter 1 for Finding Area of Triangle.")
print("Enter 2 for Finding Area of Rectangle.")
print("Enter 3 for Using Calculator")
print("Enter 4 for Finding Area of Circle.")
print("Enter 5 for Using Arithmetic Progression Tools.")
print("Enter 6 for Finding Simple Interest.")

command = input("Enter Desired Mode of operation: ")

# Functions

def areaoftriangle(h,b):
    area = (1/2*b*h)

    # returns area of triangle 
    return area

def areaofrec(l,b):
    print("<---------------AREA-OF-RECTANGLE------------------>")   #Area of Rectangle Module(area_rectangle)
    return l*b

def calc(num1,num2,operator):

    # checking for operators
    if operator == "+":
       return num1 + num2
       
    elif operator == "-":
        return num1 - num2
                 
    elif operator == "/":
        return num1 / num2
         
    elif operator == "*":
        return num1 *num2
              
    else:
        print("You have NOT entered any operator")
        input("Press 'Enter' to exit...")

def areaofcircle(radius):
    return round((2*math.pi*radius**2),2) 

def ap():
    print("<---------------ARITHMETIC-PROGRESSION----------------->")  #Arithmetic Progression(ap)
    print("What would you like to find?")
    print("Enter 1 for Finding nTH Term of AP")
    print("Enter 2 for Finding Sum of AP to nTh term")

    # Taking user input
    command =  input("Enter Which Ever Operation You Would Like To Perform: ")

    # nth term solver function
    def nth_term():
        print("<-------------FINDING-THE-NTH-TERM---------------->") #Finding the nTH term of AP(ap_nth_term)

        a = float(input("Enter the a of FIRST term of the AP: "))
        n = float(input("Enter the nTH term you want to find: "))
        d = float(input("Enter Common Difference of AP: "))
        nth_term = (a+(n-1)*d)

        print(f"The nTH term of AP is: {nth_term}")
        input("Press 'Enter' to exit...")

    # sum of ap to nth term solver
    def sum_of_ap_to_nth_term():
        print("<------------SUM-TILL-NTH-TERM-------------->")  #Finding Sum till nTH term of AP(ap_sum_nth_term)

        a = float(input("Enter the FIRST Term of AP: "))
        d = float(input("Enter the COMMON DIFFERENCE of AP: "))
        n = float(input("Enter the nTH term you want to find the sum till: "))

        s = (n/2) * (2 * a + (n - 1) *d)

        print(f"The sum till the {n}th term should be: {s}")
        input("Press 'Enter' to exit...")

    if command == "1":
        nth_term()
        
    elif command == "2":
        sum_of_ap_to_nth_term()

def si(p,r,t):
    # calculating simple interest
    return p*(1+r*t)
    

if command == "1":
    print("<--------------AREA-OF-TRIANGLE----------------->")    #Area of Triangle Module(area_triangle)

    # taking user input
    h = float(input("Enter the Height of the Triangle: "))
    b = float(input("Enter the Lenght of Base of the Triangle: "))
    unit = input("Enter the Unit of measurement(either cm,mm,m,etc): ")

    # calculated area
    area = areaoftriangle(h,b)
    
    # printing the answer
    print(f"THE AREA FOR THE TRIANGLE SHOULD BE: {area} {unit}^2")
    input("Press 'Enter' to exit..")

elif command == "2":
    # taking user input
    l = float(input("Enter Lenght of the Rectangle:"))
    b = float(input("Enter the Breadth of the Rectangle:"))
    unit = input("Enter the Unit the lenght and breadth of the Rectangle are in(either cm,mm,m,etc): ")

    # calling areaofrec() function 
    area = areaofrec(l,b)

    # printing the result
    print(f"The Area of the Rectangle should be : {area} {unit}^2")
    input("Press 'Enter' to exit...")

elif command == "3":

    print("<---------------CALCULATOR----------------->")   #Simple Python calc(py_calc)
    
    print("Enter '+' for Addition")
    print("Enter '-' for Subtraction")   
    print("Enter '/' for Division")
    print("Enter '*' for Multiplication")

    # taking user input
    operator = str(input("entrator either '+ - * /': "))
    num1 = int(input("Enter Number one: "))
    num2 = int(input("Enter Second one: "))

    # calling calc() function
    result = calc(num1,num2,operator)
    
    #printing the result
    print(f"The correct Answer should be: {result}")
    input("Press 'Enter' to exit...")
    
elif command == "4":

    print("<---------------AREA-OF-CIRCLE----------------->")       #Area if Circle Module(area_circle)

    # taking user input
    radius = int(input("Enter the Radius of the Circle you want to find the Area of: "))
    unit = str(input("Enter the Unit of the Radius(either cm,mm,m): "))

    if unit == "m" or "cm" or "mm":
        print("Working on it,please wait... ")
    else:
        print(f"{unit} is not a valid unit or is yet to be implemented.")
        input("Press 'Enter' to exist")

    # calculated area
    area = areaofcircle(radius)

    print(f"The Area of the Circle should be: {area} {unit}^2 ")
    input("Press 'Enter' to exit...")

elif command == "5":
    # calling the ap function
    ap()
       
elif command == "6":

    print("<------------SIMPLE-INTEREST-------------->") #Simple Interest Module

    # taking user input
    p = int(input("Enter Principle: "))
    r = int(input("Enter Annual Interest Rate: "))
    t = int(input("Enter Time(in years)): "))
    unit = input("What is the Unit of Currency?: ")

    # calling si() function
    Si = si(p,r,t)
    

    print(f"The Simple Interest Should be {Si} {unit}.")
    print("Press 'Enter' to exit...")

else:
    print("The Type of operator you want is not available right now or is yet to be implemented.")
    input("Press 'Enter' to exit...")
