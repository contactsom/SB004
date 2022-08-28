print("This is example for File Handling Lab-3 in python")
print("****** START- FILE HANDLING ********")

# Write in to file
f=open("abc.txt",'a')
f.write("I am Line Number One in Book File \n")
f.write("I am Line Number Two in Book File \n")
f.write("I am Line Number Three in Book File \n")
print("Data Written successfully")
f.close()
