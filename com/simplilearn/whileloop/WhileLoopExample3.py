print("****** START- WHILE Termination ********")


myString="ABCD"
k=0
print(len(myString)) #4

while (k<len(myString)): # It is traversing each character from start to end k =2
    print("I am Statement 1")

    if(myString[k] == 'C'): # If 'H' character found in given string than increase the value of K by 1
        print("I am statement 2")
        k = k+1
        print("I am statement 3")
        break # stop the remaning execution
    print("I am statement 4")
    print("________________")
    k=k+1 # 4

print("****** END- WHILE Termination ********")