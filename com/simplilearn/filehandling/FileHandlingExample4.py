print("This is example for File Handling Lab-4 in python")
print("****** START- FILE HANDLING ********")
#f=open("mylistfile.txt",'w') # Replace the existing data and write new data on each execution
f=open("mylistfile.txt",'a') # Keep the existing data and write the new data on each execution
list=["A\n","B\n","C\n","D\n"]
f.writelines(list)
print("*** Data of List added in to file successfully")
f.close()