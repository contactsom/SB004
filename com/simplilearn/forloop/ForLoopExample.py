print("This is example of For Loop in python")

print("****** START- FOR LOOP ********")

# For loop over List
myPrograming = ["JAVA","PYTHON","ANGULAR","REACT",".NET"]
               # 0    ,1        ,2        ,3      ,4
print(myPrograming)

print("____________________________")
for var1 in myPrograming:
    print(var1)
print("____________________________")
# var1 = myPrograming [0] = JAVA
# var1 = myPrograming [1] = PYTHON
# var1 = myPrograming [2] = ANGULAR
# var1 = myPrograming [3] = REACT
# var1 = myPrograming [4] = .NET
# var1 = myPrograming [5] = no value , Hence it will terminate the loop in 4th index

print("Index - 0 :" + myPrograming[0])
print("Index - 1 :" + myPrograming[1])
print("Index - 2 :" + myPrograming[2])
print("Index - 3 :" + myPrograming[3])
print("Index - 4 :" + myPrograming[4])
#print("Index - 5 :" + myPrograming[5])

print("___________For loop over Set_________________")
#For loop over Set
myProgramingSet = {"JAVA","PYTHON","ANGULAR","REACT",".NET"}

for var2 in myProgramingSet:
    print(var2)

print("___________For loop over tuple _________________")
#For loop over tuple
myProgramingtuple = ("JAVA","PYTHON","ANGULAR","REACT",".NET")

for var3 in myProgramingtuple:
    print(var3)

print("___________For loop over Dictionary _________________")
#For loop over Dictionary
# key : Roll , Value : Name
stuNameRoll = {
                1: "Ashok",
                2: "kumaraniket1432",
                3: "Shibanijoshi94158",
                4: "Shubham",
                5: "Emily"
              }
print("___________Print Key from Dictionary _________________")
for k1 in stuNameRoll:
    print(k1)

print("___________Print Value from Dictionary _________________")
for abc in stuNameRoll:
    print( stuNameRoll [abc] ) # provide the value for key- abc
    # abc hold key or value - key

#print(stuNameRoll[1]) = Ashok
#print(stuNameRoll[2]) = kumaraniket1432
#print(stuNameRoll[3]) = Shibanijoshi94158

print("___________Print Value from Dictionary using values  _________________")
for key2 in stuNameRoll.values():
    print(key2)

print("___________Print Value from Dictionary using items  _________________")
for key , value in stuNameRoll.items():
    print(key , value)

#what if we this for look without .items()

print("___________Print Value from String Using For loop _________________")
str1="abcdef"
print(str1)
for s1 in str1:
    print(s1)
print("___________Manually Print the String _________________")
myString="ABCD" # 10000 Character

print(myString[0]) #A
print(myString[1]) #B
print(myString[2]) #C
print(myString[3]) #D
# ==
# A == A = true
# B == B = true
# C == C = true
# A == a = false # case sencitive
# a == a = true




print("****** END- FOR LOOP ********")