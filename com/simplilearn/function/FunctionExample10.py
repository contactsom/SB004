print("This is example of For Function with multiple Return List  Lab 10 in python")
print("****** START- FUNCTION ********")

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div

result=calc(90,10)
print(result)

# I can iterate the value on by one also

for i in result:
    print(i)