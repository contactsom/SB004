print("This is example for EXCEPTION HANDLING-9 in python")
print("****** START- EXCEPTION HANDLING ********")
try:
    print("This is try block")
    print(10/0)
except NameError:
    print("I am Except")
finally:
    print("I am Finally")