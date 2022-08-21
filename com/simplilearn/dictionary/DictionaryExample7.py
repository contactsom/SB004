print("This is example for DICTIONARY LAB 7 in python")
print("****** START- DICTIONARY ********")
# Access the Dict

phoneDict= {
                1:"APPLE",
                2:"BOOK",
                3:"CAT",
                4:"DOG",
            }
print("------------------")

print(phoneDict[1])
print(phoneDict[2])
print(phoneDict[3])
print(phoneDict[4])

countryDict= {
                "A":"APPLE",
                "B":"BOOK",
                "C":"CAT",
                "D":"DOG",
            }
print("------------------")
print(countryDict["A"])
print(countryDict["B"])
print(countryDict["C"])
print(countryDict["D"])


print("---------get()---------")
phoneDict= {
                1:"APPLE",
                2:"BOOK",
                3:"CAT",
                4:"DOG",
            }

print(phoneDict.get(1))
print(phoneDict.get(2))
print(phoneDict.get(3))
print(phoneDict.get(4))

print("------------ Get the Key's")
# We pass the KEY and got the respective Value

# But I want only key's

phoneDict1= {
                1:"APPLE",
                2:"BOOK",
                3:"CAT",
                4:"DOG",
            }
keys=phoneDict1.keys()
print(keys)

print("_________________________")
countryDict1= {
                "A":"APPLE",
                "B":"BOOK",
                "C":"CAT",
                "D":"DOG",
            }

keys1=countryDict1.keys()
print(keys1)

# I want only Values
print("_______________ Values()")
countryDict2= {
                "A":"APPLE",
                "B":"BOOK",
                "C":"CAT",
                "D":"DOG",
            }

values=countryDict2.values()
print(values)


# I want Items
print("______________ items()")

countryDict3= {
                "A":"APPLE",
                "B":"BOOK",
                "C":"CAT",
                "D":"DOG",
            }

items=countryDict3.items()
print(items)




