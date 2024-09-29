
#runs the ap sub files

print("<---------------ARITHMETIC-PROGRESSION-------------------->")

print("What would you like to find?")
print("Press 1 for Finding nTH Term of AP")
print("Press 2 for Finding Sum of AP to nTh term")

command =  input("Enter Which Ever Operation You Would Like To Perform: ")

if command == "1":
    import sys
    sys.path.append("../ap_resources")
    from ap_resources import ap_nth_term

elif command == "2":
    import sys
    sys.path.append("../ap_resources")
    from ap_resources import ap_sum_nth_term

else:
    print("You have not entered valid mode of operation,try again.")
