
print("*_________While Loop in String 2 ______________*")

myString="ABCD"
k=0
print(len(myString)) #4

while (k<len(myString)): # It is traversing each character from start to end k =2
    print("I am Statement 1")

    if(myString[k] == 'C'): # If 'H' character found in given string than increase the value of K by 1
        print("I am statement 2")
        k = k+1 # 3
        print("I am statement 3")

    print("I am statement 4")
    print("________________")
    k=k+1 # 4

# Iteartion 1:
# Line 30 : true
# Line 31 : print("I am Statement 1")
# Line 32 : A == C => false
# Line 36 , 37 , 38 , k =1

# Iteartion 2:
# Line 30 : true
# Line 31 : print("I am Statement 1")
# Line 32 : B == C => false
# Line 36 , 37 , 38 , k = 2

# Iteartion 3:
# Line 30 : true
# Line 31 : print("I am Statement 1")
# Line 32 : true
# Line 33, 34, 35
# Line 36, 37, 38
