print("This is example for File Handling Lab-7 in python")
print("****** START- FILE HANDLING ********")
# Read the data Line by Line  From the file
f=open("data.txt",'r')

line1=f.readline()
print(line1,end='')

line2=f.readline()
print(line2,end='')

line3=f.readline()
print(line3,end='')

f.close()