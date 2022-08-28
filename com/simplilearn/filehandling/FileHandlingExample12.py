print("This is example for File Handling Lab-12 in python")
print("****** START- ZIP FILE HANDLING ********")

from zipfile import *
f=ZipFile("simp.zip",'w',ZIP_DEFLATED)
f.write("abc.txt")
f.write("book.txt")
f.write("employee.txt")
f.write("mylistfile.txt")
f.close()
print("Zip file created successfully")
