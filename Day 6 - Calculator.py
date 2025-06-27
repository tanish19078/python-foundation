# Day 6 - Mini Project: Simple Calculator 🧮

# 🔢 Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "⚠️ Error: Cannot divide by zero!"
    return x / y

# 🧠 Main calculator logic
print("🧮 Welcome to the Simple Calculator!")

while True:
    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "5":
        print("👋 Exiting calculator. Goodbye!")
        break

    if choice not in ("1", "2", "3", "4"):
        print("❌ Invalid choice. Try again.")
        continue

    # Get input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Match operation
    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)

    print("✅ Result:", result)
