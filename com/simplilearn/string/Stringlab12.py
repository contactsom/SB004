print("This is example is for STRING Slicing - Lab-12 in python")
print("****** START- STRING Slicing ********")

myString = "ABCDEFGHI"
#String  =  A, B, C, D, E, F, G, H, I,
# Index  =  0, 1, 2, 3, 4, 5, 6, 7, 8
print(myString) #ABCDEFGHI
print(myString[2:7]) #CDEFG # from 2 : to (7-1)
# [M:N]
# [FROM:TO]
# Start Index[M] or From : Mth Index Character Include
# End Index[N]   or To : [N-1]th Index Character Include
print("[1:5]- "+ myString[1:5]) # BCDE # from 1 : to (5-1)=4
print("[0:0]- "+ myString[0:0]) # Starting from 0 and Ending to 0=> You are not traversing , Work Done is 0
print("[0:8]- "+ myString[0:8]) # ABCDEFGH
print("[0:80]- "+ myString[0:80]) # ABCDEFGHI : From 0 and To 79
print("[0:9]- "+ myString[0:9]) # ABCDEFGHI
print("[:9]- "+ myString[:9]) # ABCDEFGHI
print("[2:]- "+ myString[2:]) # CDEFGHI

#print("[80]- "+ myString[80]) # Error

print("######## -Ve Index Slicing ########")
######## -Ve Index Slicing
myString1 = "ABCDEFGHI"
#String  =  A, B, C, D, E, F, G, H, I,
# Index  = -9,-8,-7,-6,-5,-4,-3,-2,-1
print("[-0:-0]"+myString1[-0:-0]) #
print("[-1:-0]"+myString1[-1:-0]) #
print("[-1:-1]"+myString1[-1:-1]) # -1:-(1-1)=   -1:-0

#print(myString1[-1:-4]) #
# -8 > -2 = False
# -9 < -1 = True
# Upper Index < Lower Index [Should be for -Ve Indexing]
print("[-8:-2]"+myString1[-8:-2]) # BCDEFG
print("[-1:-4]"+myString1[-1:-4]) #













print("****** END- STRING Slicing ********")