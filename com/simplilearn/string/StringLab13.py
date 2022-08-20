print("This is example is for str.find()  - Lab-13 in python")
print("START-******str.find() ******")

str1="Mayur Bathvar"
print(str1.find("Mayur")) # this method will return the Start index

str2="ABCD EFG"
    # 0, 1, 2, 3, 4, 5, 6, 7
    # A, B, C, D,    E, F, G
print(str2.find("E")) #5

str3="ABCD EFG"
    # 0, 1, 2, 3, 4, 5, 6, 7
    # A, B, C, D,    E, F, G
print(str3.find("AB")) #

str4="ABCD EFG"
    # 0, 1, 2, 3, 4, 5, 6, 7
    # A, B, C, D,    E, F, G
print("######")
print(str4.find("BA")) #-1
print("END-******str.find() ******")


