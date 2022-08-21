print("This is example for SET Lab 6 in python")
print("****** START- SET Lab6 ********")

mySet1 ={"ONE","TWO","THREE","FOUR"}
mySet2 ={1,2,3,4}

mySet1.update(mySet2) #
print(mySet1) # {1, 'TWO', 2, 3, 4, 'FOUR', 'THREE', 'ONE'}
print(mySet2)

# Update
#mySet1 ={"ONE","TWO","THREE","FOUR"}
#mySet1 ={"ONE","TWO","THREE","FIVE"} # Replacing from "FOUR" to "FIVE" => This is wrong in Set. Why? Because set is unchangable

#mySet1 ={"ONE","TWO","THREE","FOUR"}
#mySet1 ={"ONE","TWO","THREE","FOUR","FIVE"} # Update the Set with new element # Acceptable


print("****** END- SET Lab6 ********")
