print("This is example for EXCEPTION HANDLING-8 in python")
print("****** START- EXCEPTION HANDLING ********")
try:
    print("This is try block")
    print(10/2)
except ZeroDivisionError:
    print("I am Except")
finally:
    print("I am Finally")