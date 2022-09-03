#2. Creating a Thread by extending Thread class

from threading import *
class CreateThread2(Thread):

    def run(self):
        for i in range(5):
            print("Child Thread-1")


t=CreateThread2()
t.start()

for i in range(5):
    print("MAin Thread-1")