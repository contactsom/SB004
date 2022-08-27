print("This is example for Reduce Function Lab 1 in python")
print("****** START- REDUCE FUNCTION ********")
# reduce() - Reduce the sequence of element in to ONE by applying some business rule.
# and it is abalable in functools funcgtions

from functools import *
mylist=[1,2,3,4,5]

result=reduce(lambda a,b:a+b,mylist)
print(result)


result1=reduce(lambda a,b:a*b,mylist)
print(result1)
#range(1,100) - 1,2,3,4,5,6,7,8,9,.................100

result2=reduce(lambda a,b:a*b,range(1,100))
print(result2)

result3=reduce(lambda a,b:a+b,range(1,100))
print(result3)

