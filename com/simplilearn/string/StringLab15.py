print("This is example is for  [::]  Lab-15 in python")

myString = "ABCDEFGHI"
#String  =  A, B, C, D, E, F, G, H, I,
# Index  =  0, 1, 2, 3, 4, 5, 6, 7, 8
# Index  = -9,-8,-7,-6,-5,-4,-3,-2,-1
# Interval 1 = 1,2,3,4,5,6,7 ........
# Interval 2 = 1 , 3 5 7 9 11 13 ......

#print("[1::5]"+myString[1::5]) # BG
print("[::-1]"+myString[::-1]) # IHGFEDCBA # -Ve says that move towards - infinity and number (1) says that it is interval
print("[::-2]"+myString[::-2]) # IGECA
print("[::-3]"+myString[::-3]) # IFC
print(myString)