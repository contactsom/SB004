print("This is example for Nested Function Lab 1 in python")
print("****** START- NESTED FUNCTION ********")

def outer():
    print("I am Outer")
    def inner():
        print("I am inner")

    inner()
outer()
#inner()