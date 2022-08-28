print("This is example for File Handling Lab-9 in python")
print("****** START- FILE HANDLING ********")

# Write in to file
with open("employee.txt",'w') as f:
    f.write("Vidhi \n")
    f.write("Suganthi \n")
    f.write("Mayur \n")
    f.write("Ashok \n")
    f.write("Hrushikesh \n")
    f.write("Divya \n")
    f.write("Vikram \n")
    f.write("Rajesh \n")
    print("Is File Closed : ", f.closed)
print("Is File Closed : ", f.closed)
print("Data Written successfully")

