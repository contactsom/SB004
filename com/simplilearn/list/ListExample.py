print("This is example for LIST in python")
print("****** START- LIST ********")

# 1. Create the Integer List
intList=[1,2,3,45,6,78,]
print(intList) #[1, 2, 3, 45, 6, 78]
print(type(intList))

print("___________________________")
# 2. Creat the Blank List
blankList=[]
print(blankList)
print(type(blankList))

print("___________________________")
# 3. Create the String List
stringList=["INDIA","USA","UK"]
print(stringList)
print(type(stringList))

# How to fetch the data one by one : Refer for loop example

print("___________________________")
# 4. Create the String List having duplicate data
stringDuplicateList=["INDIA","USA","UK","INDIA","USA","UK"]
print(stringDuplicateList)
print(type(stringDuplicateList))

print("___________________________")
# 5. Create the list which hold the String and Int data both
stringIntList=["INDIA","USA","UK",1,2,3,45]
print(stringIntList)
print(type(stringIntList))

# 6.Indexing of the List
print("___________________________")
myIndexList=[0,1,2,3,4,5]
print(myIndexList)
print(myIndexList[4]) # 4

# 7. MultiDimentional List
list1=[4,5,6]
# Index : 0,1,2
print(list1[0]) # 4
print(list1[1]) # 5
print(list1[2]) # 6

list2 = [4,5,6]
list3 = [1,2,3]
list4 = [11,12,13]

multiList = [
                [4,5,6], # Index 0
                [1,2,3], # Index 1
                [11,12,13] # Index 2
            ]

# Index    : 0 ,1, 2
# Length   : 3




print("****** END- LIST ********")