collection = {1, 2, 3, 4, 5, "hello", "world", 6, 5}

print(collection) #printing the whole set
print(type(collection)) 
print(len(collection)) #printing total number of items


#set methods_______________________

value = set() #empty set

value.add(1) #adding a single value to the set
value.add(2) #adding a single value to the set
value.add(3) #adding a single value to the set

#value.remove(2) #removing a specific value from the set

#value.clear() #removing all the values from the set

#value.pop() #removing a random value from the set
print(value) 

set1 = {1, 2, 3 , 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) #union of two sets
print(set1.intersection(set2)) #intersection of two sets