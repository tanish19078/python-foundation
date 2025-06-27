# Day 3 - Conditions (if, elif, else)

# 🧠 Learning Goals:
# - Understand if/else logic
# - Use comparison operators
# - Write simple decision-making programs

print("=== Welcome to the Age Checker ===")

# 🎯 Get age input from user
age = int(input("Enter your age: "))

# 🔍 Conditional logic
if age < 13:
    print("You're a child.")
elif age < 20:
    print("You're a teenager.")
elif age < 60:
    print("You're an adult.")
else:
    print("You're a senior.")

# 🧪 More examples: even or odd
print("\n=== Even or Odd Checker ===")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is Even.")
else:
    print(f"{number} is Odd.")

# ✅ Boolean condition with string input
print("\n=== Login Example ===")
username = input("Enter your username: ")

if username == "tanish":
    print("Welcome back, Tanish!")
else:
    print("Access denied.")

# 🔄 Summary:
# - Use `if`, `elif`, `else`
# - Use `==`, `!=`, `<`, `>`, `<=`, `>=` for conditions
