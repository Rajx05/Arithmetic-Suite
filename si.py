#Simple Interest Module

print("<------------SIMPLE-INTEREST-------------->")

p = int(input("Enter Principle: "))
r = int(input("Enter Annual Interest Rate: "))
t = int(input("Enter Time(in years)): "))
unit = input("What is the Unit of Currency?: ")

a = p*(1+r*t)

print(f"The Simple Interest Should be {a} {unit}.")