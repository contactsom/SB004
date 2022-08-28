import imports as imports

print("This is example for EXCEPTION HANDLING-10 in python")
print("****** START- EXCEPTION HANDLING ********")

import os
try:
    print("This is try block")
    os._exit(0) # Forcely termenating the code
except NameError:
    print("I am Except")
finally:
    print("I am Finally")