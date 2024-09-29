
#This will find the sum till the nTH term

print("<------------SUM-TILL-NTH-TERM-------------->")

a = float(input("Enter the FIRST Term of AP: "))
d = float(input("Enter the COMMON DIFFERENCE of AP: "))
n = float(input("Enter the nTH term you want to find the sum till: "))

s = (n/2) * (2 * a + (n - 1) *d)

print(f"The sum till the {n}th term should be: {s}")