# Simple function
def greet(name): 
    print(f"Hello, {name}")
greet("shree")  # Output: Hello, shree
greet("patel") # Output: Hello, patel

 # Function with return value
def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)  # Output: Sum: 8


def greet(name="shree"):
    print(f"Hello, {name}")
greet()  # Output: Hello, shree
greet("shree,kant")  # Output: Hello, shree,kant


# Function with default parameter
def power(base, exp=2):
    return base ** exp
print(power(5))  # Output: 25 (default exponent is 2)
print(power(5, 3))  # Output: 125 (5 raised to the power of 3) 
