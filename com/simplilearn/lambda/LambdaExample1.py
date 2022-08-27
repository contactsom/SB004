print("This is example for Lambda Function Lab 1 in python")
print("****** START- LAMBDA FUNCTION ********")

def addTwo(a,b):
    c=a+b
    return c
result=addTwo(20,10)
print(result)

print("***** With Lambda Function********")

result1=lambda a,b:a+b
print(result1(20,10))


print("**********************************")

squre=lambda a:a*a
print(squre(6)) # 36


print("to find the biggest number")

# to find the biggest number
biggest=lambda a,b:a  if a>b else b
print(biggest(20,30))
print(biggest(10,6))