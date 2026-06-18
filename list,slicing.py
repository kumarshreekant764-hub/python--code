#list slicing
marks = [95, 88, 76, 92, 85, 100, 67, 89, 73, 84]
print(marks[1:4])
print(marks[:5])
print(marks[5:])
print(marks[-3:-1])



#list methods
list = [2, 3, 1, 8, 4, 7, 5, 6]
list.append(9)
print(list)

list.sort()
print(list)

list.sort(reverse = True)
print(list)

list.reverse()
print(list)

list.insert(2, 4)
print(list)

list.remove(8)
print(list)

list.pop(4)
print(list)

