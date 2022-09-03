from threading import *
#3. Creating a Thread without extending Thread class
class CreateThread3:

    def display(self):
        for i in range(5):
            print("Child Thread-1")

obj=CreateThread3()
t=Thread(target=obj.display)
t.start()

for i in range(5):
    print("Main Thread")


