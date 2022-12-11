"""
os.chdir()
The os module provides the chdir() function to change the current working directory.
"""
import os

print("Before Change My Directory ",os.getcwd())

os.chdir("/Users/om/SB004/com/simplilearn/osmodule/lab3")

print("After Change My Directory ",os.getcwd())