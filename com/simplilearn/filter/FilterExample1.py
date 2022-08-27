print("This is example for filter Function Lab 1 in python")
print("****** START- FILTER FUNCTION ********")

def isEven(a):
    if a%2==0:
        return True
    else:
        return False

#result=isEven(3)
#print(result)

myList = [1,3,6,2,8,10]
#resultList=list(filter(isEven(myList)))

resultList=list(filter(isEven,myList))
print(resultList)
