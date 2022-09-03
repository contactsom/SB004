class Test:
    def __init__(self):
        print("I am Constructor")

    def display(self):
        print("I am display")

# Constructor will getting called only once per object
t1= Test()
t2= Test()
t3= Test()
t4= Test()
t1.display()
#t1.display()
