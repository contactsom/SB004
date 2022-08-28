print("This is example for EXCEPTION HANDLING-2 in python")
print("****** START- EXCEPTION HANDLING ********")

print("I am Statement 1")
try:
    print(10/0) # Risky
except ZeroDivisionError:
    print(10/2)
print("I am Statement 3")