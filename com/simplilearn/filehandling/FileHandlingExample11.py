print("This is example for File Handling Lab-11 in python")
print("****** START- IMAGE FILE HANDLING ********")
f=open("Simplilearn_Logo.jpg",'rb')
f1=open("Simplilearn_NEW_Logo.jpg",'wb')
bytes=f.read()
f1.write(bytes)
print("New Image is getting created")


#print(bytes)
