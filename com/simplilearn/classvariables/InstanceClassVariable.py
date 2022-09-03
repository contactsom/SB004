class InstanceClassVariable:
    def __init__(self):
        self.a=10
        self.b=20

    def display(self):
        print(self.a)
        print(self.b)

obj1=InstanceClassVariable()
obj1.display()
print("***********")
print(obj1.a,obj1.b)