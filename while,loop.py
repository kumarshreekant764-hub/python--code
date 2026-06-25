#count = 1 
#while count <= 5:
#    print("hlo")
#    count += 1

#print("Done counting!")

#print("counting from 1 to 100")
i = 1
while i <= 100:
#    print("count :", i)
    i += 1\
    
#print("loop ended")


#print("counting from 100 to 1")
i = 100
while i >= 1:
#    print("count :", i)
    i -= 1

#print("loop ended")


#print the multiplication table of a number n.
#n = int(input("Enter a number : "))
i = 1
while i <= 10:
#    print (n * i)
    i += 1

#print("table completed")


#print the elements of the following list using loop :
#[1,4, 9, 16, 25, 36, 49, 64, 81, 100]

num = [1,4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0
while i <len(num):
#    print(num[i])
    i+= 1

#print("Elements printed")




#search for a number X in this tuple using loop :
#[1,4, 9, 16, 25, 36, 49, 64, 81, 100]

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

X = 36

#i = 0
#while i < len(num):
#    if num[i] == X:
#        print("found at idx", i)
#    i += 1

#print("search completed")


#break & continue statement in while loop__________

idx = 1
while idx <= 10:
#    print(idx)
    if(idx == 5):
        break
    idx += 1

print("loop ended")


i = 0 
while i <= 5:
    if(i == 3):
        i += 1
        continue  #skip any number which is equal to 3
    print(i)
    i += 1