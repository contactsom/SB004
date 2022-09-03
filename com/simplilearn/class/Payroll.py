class Payroll:
    ''' This is Payroll  Class which holds all the pay related info'''
    print()
    def __init__(self): # Constructor
        self.name='simplilearn'
        self.salery=50
        self.id=101

    def pay(self): #Method
        print("I am Method from payroll Class")
        print("My Payroll Name is ",self.name)
        print("My Salary is ",self.salery)
        print("My ID is",self.id)


p1=Payroll()
p1.pay()
