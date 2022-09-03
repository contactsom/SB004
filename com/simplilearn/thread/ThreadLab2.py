from threading import *

def test():
    print("Child Thread")

t=Thread(target=test)
t.start()

print("Main thread Identification Number : ",current_thread().ident)
print("My thread Identification Number : ",t.ident)