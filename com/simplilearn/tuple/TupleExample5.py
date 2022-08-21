print("This is example for TUPLE lab 5 in python")
print("****** START- TUPLE  lab 5 ********")
# Update the Tuple
# You can not update the tuple directoly
# How ?
# Convert the tuple in to list and then update
a=(1,2,3,4,5)
print("Before Update")
print(a)
print("After Update")
#a[2]=36       # I am updating 3 to 36 ERROR

a1=list(a)#1. Convert tuple to list
a1[2]=36 # I am List updating 3 to 36
# Return to actual tuple
# Convert back from list to tuple
a=tuple(a1)
print(a)
print(type(a))

print("-------------------------------------------")

frutsTuple=("APPLE","BANANA","GREPS")
print(frutsTuple)
# I want to update BANANA to orange

listFruts=list(frutsTuple) # Converting to list
listFruts.append("orange")
frutsTuple=tuple(listFruts) # Converting back to tuple
print(frutsTuple)











