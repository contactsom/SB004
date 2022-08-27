print("This is example of For Function with multiple Return  Lab 9 in python")
print("****** START- FUNCTION ********")

def getSumSub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub


x,y=getSumSub(30,20)
# here x holds the value of sum
# y holds the value of sub
print(x,y)