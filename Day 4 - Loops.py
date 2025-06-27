# Day 4 - Loops (for, while)

# 🧠 Learning Goals:
# - Understand "for" and "while" loops
# - Use "range()" for iteration
# - Learn about break, continue

# 🔁 For loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# 🎯 Loop through a list
fruits = ["apple", "banana", "mango"]
print("\nMy fruits list:")
for fruit in fruits:
    print(fruit)

# 📦 Using break
print("\nStop loop if 'banana' is found:")
for fruit in fruits:
    if fruit == "banana":
        print("Banana found! Stopping loop.")
        break
    print("Checking:", fruit)

# 🌀 While loop
print("\nCountdown from 5:")
count = 5
while count > 0:
    print(count)
    count -= 1

print("Liftoff!")

# ❌ Infinite loop warning (commented out)
# while True:
#     print("This will run forever...")

# 🧪 continue statement
print("\nPrint odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# 🔄 Summary:
# - `for` loops: best for counting or iterating
# - `while` loops: best when condition must be checked
# - `break`: exit the loop
# - `continue`: skip the current iteration
