print("****** Start- LIST Lab 4 ********")

froots=["APPLE","MANGO","BANANA"]
print("---- Before Delete")
print(froots)

print("---- After Delete")
froots.remove("BANANA") # We pass the List element
print(froots)

print("____________pop()__________________")


myLits=["A","B","C","D","E"]
# I want to delete the list element from the index of 3 i.e D
print("Before Deleting the data Using Index Value")
print(myLits)

print("After Deleting the data Using Index Value")
myLits.pop(3)
print(myLits)


print("###########################")
stringList=["INDIA","USA","UK"]
stringList.pop()
#stringList.remove(3)
print(stringList)


print("____________del Index__________________")

countryList=["INDIA","USA","UK"]
print("###### Before Delete")
print(countryList)

print("###### After Delete")
del countryList[1]
print(countryList)

print("____________del no Index__________________")

countryList=["INDIA","USA","UK"]
print("###### Before Delete")
print(countryList)

print("###### After Delete")
del countryList
#print(countryList)


print("____________clear__________________")

countryList=["INDIA","USA","UK"]
print("###### Before Delete")
print(countryList)

print("###### After Delete")
countryList.clear()
print(countryList)

# Remove - delete the data based on data
# pop(index) - delete the data based on index
# pop() - delete the data from last
# del(index) - delete the data based on index
# del - Hard list delete
# Differences between del & clear


















print("****** End- LIST Lab 4 ********")