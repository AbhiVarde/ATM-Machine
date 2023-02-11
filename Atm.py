print("\n**  Welcome to Bharat Bank  **\n")
p = int(input("Please Enter Your 4 digit PIN No: "))
t = 50000
if (p == 1254):
    print("\n1 -> Withdraw")
    print("2 -> Balance Enquiry")
    print("3 -> Fast Cash")
    c = int(input("\nPlease choose transactions: "))
    if (c == 1):
        w = int(input("\nEnter Withdraw amount: "))
        if (w < t and w % 100 == 0):
            print("Please take your amount: ", w)
        else:
            print("Invalid cash !!")
    elif (c == 2):
        print("\nYour available balance: ", t)
    elif (c == 3):
        print("\n1 -> 5000")
        print("2 -> 10000")
        print("3 -> 20000")
        print("4 -> 40000")
        u = int(input("\nEnter Fast Cash option: "))
        if (u == 1 and 5000 < t):
            print("Please take cash 5000")
        elif (u == 2 and 10000 < t):
            print("Please take cash 10000")
        elif (u == 3 and 20000 < t):
            print("Please take cash 20000")
        elif (u == 4 and 40000 < t):
            print("Please take cash 40000")
        else:
            print("Invalid Fast Cash option !!")
    else:
        print("\nWrong choice !!")
else:
    print("\nWrong PIN No !!")
