# Create a dictionary
person = {"name": "shree", "age": 20, "city": "new delhi"}

# Access values
print(person["name"])  # Output: shree
print(person["age"])   # Output: 20
print(person["city"])  # Output: new delhi


# Modify a value
person["age"] = 21
print(person["age"])   # Output: 21


# Add a new key-value pair
person["email"] = "shree@example.com"
print(person["email"])  # Output: shree@example.com


# Remove a key-value pair
del person["city"]
print(person)  # Output: {'name': 'shree', 'age': 21, 'email': 'shree@example.com'}


# Length of the dictionary
print(len(person))  # Output: 3


# Check if a key exists
print("name" in person)  # Output: True
print("city" in person)  # Output: False


# Get all keys and values
print(person.keys())    # Output: dict_keys(['name', 'age', 'email'])
print(person.values())  # Output: dict_values(['shree', 21, 'shree@example.com'])
print(person.items())   # Output: dict_items([('name', 'shree'), ('age', 21), ('email', 'shree@example.com')])


# Loop through the dictionary
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: shree
# age: 21
# email: shree@example.com 



# Get all keys and values
print(person.keys())    # Output: dict_keys(['name', 'age', 'email'])
print(person.values())  # Output: dict_values(['shree', 21, 'shree@example.com'])
