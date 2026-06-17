# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Access items (index starts at 0)
int(numbers[0])
print(numbers[0])  # Output: 1
print(numbers[4])  # Output: 5


# Modify an item
numbers[2] = 99
print(numbers[2])  # Output: 99


# Add an item to the end of the list
numbers.append(11)
print(numbers)  # Output: [1, 2, 99, 4, 5, 6, 7, 8, 9, 10, 11]

# Remove an item
numbers.remove(99)
print(numbers)  # Output: [1, 2, 4, 5,6, 7, 8, 9, 10, 11]


# Length of the list
print(len(numbers))  # Output: 10

# Slicing the list
print(numbers[0:5])  # Output: [1, 2, 4, 5, 6]
print(numbers[5:10]) # Output: [7, 8, 9, 10, 11]

print(type(numbers))
