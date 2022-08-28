print("This is example for File Handling Lab-6 in python")
print("****** START- FILE HANDLING ********")
# Read the top five Data i.e Five Character  From the file
f=open("data.txt",'r')
data=f.read(4)
print(data)
f.close()