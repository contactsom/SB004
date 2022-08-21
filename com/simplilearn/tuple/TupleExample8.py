print("This is example for TUPLE lab 8 in python")
print("****** START- TUPLE  lab 8 ********")

# Unpack
frutsTuple=("orange","BANANA","GREPS")
(white,yellow,green)=frutsTuple
print(white)
print(yellow)
print(green)


print("-------------------------")
countryTuple=("Afghanistan","Bangladesh","Canada","Vietnam","Israel","South Korea")
(a,b,c,*asia)=countryTuple
print(a)
print(b)
print(c)
print(asia)