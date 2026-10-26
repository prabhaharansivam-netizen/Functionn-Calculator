print("===== WELCOME TO CALCULATOR =====")
Operation = input("What operation do you want to do (Addition, Subtraction, Multiplication or Division):")
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))

if ZeroDivisionError:
    print("Please enter a number other than 0: ")
else:
    pass

if ValueError:
    print("Only numbers allowed:")
else:
    pass

if Operation == "Addition":
    print("Solution:", (a + b))
elif Operation == "Subtraction":
    print("Solution:", (a - b))
elif Operation == "Multiplication":
    print("Solution:", (a * b))
elif Operation == "Division":
    print("Solution:", (a / b))


