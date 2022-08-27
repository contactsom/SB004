print("This is example for Local & Global Variable Lab 2 in python")

print("****** START- Local & Global Variable ********")

a=123

def fun1():
    a=456
    print(a)

fun1()

def fun2():
    print(a)

fun2()

