
#THIS WILL FIND THE NTH TERM

print("<-------------FINDING-THE-NTH-TERM---------------->")

a = float(input("Enter the a of FIRST term of the AP: "))
n = float(input("Enter the nTH term you want to find: "))
d = float(input("Enter Common Difference of AP: "))

nth_term = (a+(n-1)*d)

print(f"The nTH term of AP is: {nth_term}")

