# Day 5 - Functions

# 🧠 Learning Goals:
# - Define and call functions
# - Use parameters and return values
# - Understand scope (local vs global)

# 🛠️ Basic function
def greet():
    print("Hello, welcome to Python functions!")

greet()  # Call the function

# 🔁 Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Tanish")
greet_user("Alice")

# ➕ Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)

# 📐 Function to check if a number is even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))

# 🧪 Function that takes input and returns output
def square(number):
    return number ** 2

num = int(input("\nEnter a number to square: "))
print(f"The square of {num} is {square(num)}")

# 🔄 Summary:
# - `def` is used to define functions
# - Use parameters to pass data
# - `return` sends back a result
