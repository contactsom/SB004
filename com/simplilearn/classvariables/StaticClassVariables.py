class StaticClassVariables:
    a=10
    def __init__(self):
        print(self.a)
        print(StaticClassVariables.a)

    def display(self):
        print(self.a)
        print(StaticClassVariables.a)

obj1=StaticClassVariables()
print("*****************")
obj1.display()
