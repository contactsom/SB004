print("This is example for EXCEPTION HANDLING-3 in python")
print("****** START- EXCEPTION HANDLING ********")

print("I am Statement 1")
try:
    print(10/0) # Risky
    print("I am in TRY") # Skipped
except ZeroDivisionError:
    print(10/2)
print("I am Statement 3")

# "I am Statement 1
# 5.0
# I am Statement 3