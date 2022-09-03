#1. Creating a Thread without using any class

from threading import *

def display():
    for i in range(1,5):
        print("Child Thread")

t=Thread(target=display) # Creating the Thread
t.start() # Starting the thread

for i in range(1, 5):
    print("MAin Thread")