#for file read
f = open("code.py", "r")
data = f.read(10)

print(data)
print(type(data))
f.close()


#read one line at the time
f = open("function.py", "r")
line1 = f.readline()

print(line1)

line2 = f.readline()

print(line2)
f.close()


#file open to a write mode
f = open("code.py",  "w")

f.write("i am shree, i am reading python")
f.close()


f = open("code.py",  "a") #append mode

f.write("\ni am shree, i am reading python")
f.close()


#with syntax
with open("code.py", "r") as f:
    data = f.read()
    print(data)


#with open('code.py', "w") as f:
#    data = f.write("new data")
#    print(data)



#deleting a file

#import os

#os.remove("shree.txt")



#practice questions______________________________________

with open("practice.txt", "w") as f:
    f.write("hi everyone\nwe are learning file I/O\n")
    f.write("using java.\ni like programming in java.")


#waf that replaces all occurrences of" java " with "python" in above file.
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", 'w') as f:
    f.write(new_data)


#search if the word "learning" exists in the file or not.
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word)!= -1):
        print("found")
    else:
        print("not found")


#waf to find in which line of the file does the word "learning" occur first , print -1 if word not found
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", 'r') as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
        return -1

print(check_for_line())     


#from a file containing numbers separated by comma, printthe count of even numbers.
with open("code.py", "r") as f:
    data = f.read()
    print(data)

    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count += 1

print(count)

