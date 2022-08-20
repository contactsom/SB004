print("This is example is for str.rfind()  - Lab-14 in python")
print("START-******str.rfind() ******")

str1="ABCD EFG"
    # 0, 1, 2, 3, 4, 5, 6, 7
    # A, B, C, D,    E, F, G
print(str1.rfind("E")) # 5
print(str1.rfind("EF")) # 5
print(str1.rfind("FE")) # -1
print("_________________________")
str2="ABCABCABCABC"
#A, B, C, A, B, C, A, B, C, A, B, C"
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11
#0,3,6,9 - A's INDEX

print(str2.rfind("A")) #9
print(str2.find("A")) #

#NOTE Practice all the String Method mentioned in PPT


print("END-******str.rfind() ******")