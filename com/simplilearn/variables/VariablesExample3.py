print("This is example for Local & Global Variable Lab 3 in python")

print("****** START- Local & Global Variable ********")


a=123
b=98

def fun1():
    global a
    a=456
    print(a)
fun1() # 456

def fun2():
    print(a)
fun2() # 456

def fun3():
    print(b)
fun3() # 98
