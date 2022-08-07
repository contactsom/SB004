print("This is example for Floor Division Operator in python")

print("****** START- FLOOR DIVISION OPERATOR ********")

#Case - 1
#Where m & n tends to +infinity than it returns q.

m = 4
n = 2
mn= m // n
print(mn)
print(type(mn))
print("*_______________________*")

x = 20
y = 10
z = x//y
print(z) #2
print(type(z))

print("*_______________________*")
x1 = 20.5
y1 = 10.6
z1 = x1//y1
print(z1) #
print(type(z1))

#Case - 2
#Where m or n (not m and n) tends to -infinity & r=0 (perfectly divisible) than it returns -(q).
print("*_________CASE-2______________*")
a1=-4
b1=2
c1= a1//b1 # -2
print(c1)
print("*_______________________*")
a2 = 6
b2 = -3
c2=a2//b2
print(c2) #-2
print("*_______________________*")
a3 = 11
b3 = -1
c3=a3//b3
print(c3) #

print("*_______________________*")
a4 = 11
b4 = -11
c4=a4//b4
print(c4) #


#Case - 3
#Where m or n (not m and n) tends to -infinity and r!=0 (NOT perfectly divisible) than it returns -(q+1)
print("*_________CASE-3______________*")

a5=11
b5=-2
c5=a5//b5 # q = 5 , -(5+1) = -6
print(c5) # -6

print("*_______________________*")
a6=-90
b6= 4
c6=a6//b6 #22 i.e -(q+1) = -(22+1)
print(c6)#-23

#Case - 4
#Where m and n both tends (move towards) to -infinity then refer Case 1.
print("*_________CASE-4______________*")
a7= - 10
b7= - 5
c7=a7//b7
print(c7) #2

print("*_______________________*")
a8= - 13
b8= - 2
c8=a8//b8
print(c8) # 6

print("****** END- FLOOR DIVISION OPERATOR ********")