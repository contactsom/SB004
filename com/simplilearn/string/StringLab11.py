print("This is example is for SSTRING +Ve And -Ve Index - Lab-11 in python")
print("****** START- STRING +Ve And -Ve Index ********")

#ABCD
#String -  A, B,  C, D
#Index  -  0, 1,  2, 3 [+ve Index Representation]
#Length -  4
#Length - last Index + 1 = 3+1= 4

myString="ABCD"
print(myString[0]) # A
print(myString[3]) # D
#print(myString[4]) #IndexError: string index out of range

print("****** STRING --Ve Index of a String ********")

# -Ve Index of a String
#ABCD
#String -  A, B,  C, D
#Index  - -4,-3,-2, -1
# [-Ve Index Representation]

myString1="ABCD"
print(myString1[-1]) # D
print(myString1[-4]) # A
print(myString1[0])  # A
print(len(myString1)) # Length of this String is 4

# Difference between Zero Index  & -(Length of this String) in -Ve indexing Case
# No Differences . It is Same


print("****** END- STRING +Ve And -Ve Index ********")