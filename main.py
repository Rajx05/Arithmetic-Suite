#This will run all other files

print("<---------------------ARITHMETIC-SUITE------------------------->")

print("What would you like to do? ")
print("Enter 1 for Finding Area of Triangle.")
print("Enter 2 for Finding Area of Rectangle.")
print("Enter 3 for Using Calculator")
print("Enter 4 for Finding Area of Circle.")
print("Enter 5 for Using Arithmetic Progression Tools.")
print("Enter 6 for Finding Simple Interest.")

command = input("Enter Desired Mode of operation: ")

if command == "1":
    import area_triangle
elif command == "2":
    import area_rectangle
elif command == "3":
    import py_calc
elif command == "4":
    import area_circle
elif command == "5":
    import ap
elif command == "6":
    import si
else:
    print("The Type of operator you want is not available right now or is yet to be implemented.")
