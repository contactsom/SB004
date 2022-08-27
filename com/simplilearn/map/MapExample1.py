print("This is example for Map Function Lab 1 in python")
print("****** START- MAP FUNCTION ********")
# map() - to perform the operation on every element of the sequence and return the same number of element

mylist=[1,2,3,4,5,6,7] # 7

def doubleMe(a):
    return a*2

list1=list(map(doubleMe,mylist))

print(list1) # [2, 4, 6, 8, 10, 12, 14] # 7