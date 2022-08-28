print("This is example for EXCEPTION HANDLING-4 in python")
print("****** START- EXCEPTION HANDLING ********")
# How to Print the Exception
try:
    print(10/0)
except ZeroDivisionError as msg:
    print("Exception Occured ",msg)