#for loop using list
#list = [1, 2, 3, 4, 5]

#for val in list:
#    print(val) 


#veggies = ["carrot", "broccoli", "spinach"]
#for val in veggies:
#   print(val)


#for loop using tuple
#tuple = (1, 2, 3, 4, 5)

#for val in tuple:
#    print(val)


#for loop using string
string = "shreekant"

#for char in string:
#    if(char == 'k'):
#        print(" K Character found")
#        break
#    print(char)
#else:
#    print("No more characters left in the string")


#search for a number X in this tuple using loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36

#idx = 0
#for val in tup:
#    if (val == x):
#        print("number found at index", idx)
        
#    idx += 1


#for loop using range statement _____________

seq = range(2, 10, 2)
for i in seq:
    print(i)


#print the multiplication of table of a number n.

n = int(input("Enter a number: "))

for i in range (1, 11):
    print(n, "x", i, "=", n*i)



#for loop using pass statement--------
for i in range(10):
    pass
    print("empty loop")

for i in range(10):
    if(i == 2):
        pass
    else:
        print(i)