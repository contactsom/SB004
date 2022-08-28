print("This is example for EXCEPTION HANDLING-5 in python")
print("****** START- EXCEPTION HANDLING ********")

try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x/y)
except ZeroDivisionError:
    print("Ca't Divide with Zero")
except ValueError:
    print("PLease provid the Int value only")
