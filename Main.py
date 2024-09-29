#This will run all other files

def main():
    print("Main.py has stopped.")
    # Your main logic here

if __name__ == "__main__":
    main()


print("<--------------ARITHMETIC-SUITE--------------->")

print("Enter your needed operation:  ")
print("Press 1 for Finding Area of Triangle.")
print("Press 2 for Finding Area of Rectangle.")
print("Press 3 for Calculator.")
print("Press 4 for Finding Area of Circle.")
print("Press 5 for Using Arithmetic Progression tools.")

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
else:
    print("The Type of operator you want is not available right now.")