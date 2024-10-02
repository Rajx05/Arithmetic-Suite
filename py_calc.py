
#making a python calculator(very simple indeed)

print("<---------------CALCULATOR----------------->")

print("Enter '+' for Addition")
print("Enter '-' for Subtraction")   
print("Enter '/' for Division")
print("Enter '*' for Multiplication")

operator = input("enter your operator either '+ - * /': ")

num1 = int(input("Enter Number one: "))
num2 = int(input("Enter Second one: "))

if operator == "+":
    result = num1 + num2
    print(f"The correct Answer should be: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The correct Answer should be: {result} ")
elif operator == "/":
    result = num1 / num2
    print(f"The correct Answer should be: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The correct Answer should be: {result}")
else:
    print(f"operator {operator} is not a valid one")
