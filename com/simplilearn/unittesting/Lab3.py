def add(a,b):
    return a+b

assert add(2,5)==7,"The Sum of 2 and 5 should be 7"
assert add(3,5)==8,"The Sum of 3 and 5 should be 8"
assert add(4,6)==10,"The Sum of 4 and 6 should be 10"
assert add(4,8)!=10,"The Sum of 4 and 8 should not be 10"
assert add(5,8)>12,"The Sum of 5 and 8 should be grater than 12"
print(add(2,5))
print(add(3,5))
print(add(4,6))