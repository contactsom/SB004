print("This is example for TUPLE lab 6 in python")
print("****** START- TUPLE  lab 6 ********")

# Delete the Element
# You can not because tuple are unchangable
# But list will help you to do that

print("-------- DElete")
frutsTuple=("APPLE","BANANA","GREPS")
frutsList=list(frutsTuple) # from tuple to list converted
frutsList.remove("BANANA")
frutsTuple=tuple(frutsList)
print(frutsTuple)



