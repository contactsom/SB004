print("This is example for Local & Global Variable in python")

print("****** START- Local & Global Variable ********")

a = 10 # Global Variable

def fun1():
    #a=10 # Local Variable
    print(a)

def fun2():
    #a=10
    print(a)

def fun3():
    #a=10
    print(a)

#CAlling the finction
fun1()
fun2()
fun3()