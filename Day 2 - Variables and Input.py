# Day 2 - Variables and Input

# 🧠 Learning Goals:
# - Understand variables
# - Take input from the user
# - Do basic operations

# 📦 Variables store data in memory
name = "Tanish"
age = 17
is_student = True

print("My name is", name)
print("I am", age, "years old.")
print("Am I a student?", is_student)

print("\n--- Now let's take your input! ---\n")

# 🧾 Taking user input
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

print("Hello", user_name + "!")
print("You are", user_age, "years old.")

# 🧮 Type casting: converting input to numbers
num1 = input("\nEnter a number: ")
num2 = input("Enter another number: ")

# By default, input is a string → convert to integer
num1 = int(num1)
num2 = int(num2)

total = num1 + num2
print("The sum is:", total)

# 🎯 Bonus: f-string formatting
print(f"\nNice work, {user_name}! You just added {num1} + {num2} = {total}.")
