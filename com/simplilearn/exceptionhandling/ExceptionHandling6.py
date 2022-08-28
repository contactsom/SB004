print("This is example for EXCEPTION HANDLING-6 in python")
print("****** START- EXCEPTION HANDLING ********")

try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x/y)
except (ZeroDivisionError,ValueError):
    print("Ca't Divide with Zero or Please provide the Int value only")

