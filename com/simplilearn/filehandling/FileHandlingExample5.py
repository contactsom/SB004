print("This is example for File Handling Lab-5 in python")
print("****** START- FILE HANDLING ********")
# Read the Data From the file
f=open("data.txt",'r')
data=f.read()
print(data)
f.close()