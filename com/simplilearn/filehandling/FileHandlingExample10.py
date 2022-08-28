print("This is example for File Handling Lab-10 in python")
print("****** START- FILE HANDLING ********")
# Write a program to check whether the given file exist or not

import os,sys

fname=input("Enter File Name:")
if os.path.isfile(fname):
    print("File Exist")
else:
    print("File Not Exist")