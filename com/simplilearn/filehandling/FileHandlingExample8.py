print("This is example for File Handling Lab-8 in python")
print("****** START- FILE HANDLING ********")
# Read the data Line by Line  From the file
f=open("data.txt",'r')
lines=f.readlines()
for line in lines:
    print(line,end='')
f.close()