from threading import *
print("Before name Change")
print(current_thread().name)

current_thread().setName("Simplilearn")
print("After name Change")
print(current_thread().name)

