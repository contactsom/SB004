print("****** Start- LIST Lab 5 ********")

list1=[
        [1,2,3,4], # 0
        [9,5,7,3], # 1
        [0,1,8,5]  # 2
    ]

print(list1)
print(len(list1))

# For loop to pring the multi dim list
print("Using For Loop")
for record in list1:
    print(record)

print("Using For Loop with range and i")
for i in range(len(list1)): # 0 , 1, 2
    for j in range(len(list1[i])):
        print(list1[i][j],end=" ")
    print()

    #range(len(list))=mean
    # range (length of list)
    # till length of list
    # Traverse end of the list

####################

# Iteration 0 ,
    # Iteration 0 ,
    # Iteration 1 ,
    # Iteration 2 ,
    # Iteration 3 ,

# Iteration 1 ,
    # Iteration 0 ,
    # Iteration 1 ,
    # Iteration 2 ,
    # Iteration 3 ,

# Iteration 2 ,
    # Iteration 0 ,
    # Iteration 1 ,
    # Iteration 2 ,
    # Iteration 3 ,


print("****** End- LIST Lab 5 ********")