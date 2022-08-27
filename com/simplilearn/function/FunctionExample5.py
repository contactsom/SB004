print("This is example of For Function with Return  Lab 5 in python")
print("****** START- FUNCTION ********")


def addTwoNum():
   return 20+30

result=addTwoNum()
print(result)

print("****************")

def addTwoNum1():
   return 20+30

result=addTwoNum1()
print(result+50)


print("****************")

def addTwoNumber(a,b):
   return a+b

result=addTwoNumber(1,2)
print(result) #3


print("****************")

def addTwoNumber1(a,b):
    print("First Number is ",a)
    print("Second Number is ",b)
    return a+b
    print("I am your Work") # Skipped

result=addTwoNumber1(1,2)
# result variable is reciving the data returned from function called addTwoNumber1
print("Result-",result) #3

