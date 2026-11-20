# Calculator Program
# Perform addition, subtraction, multiplication, and division using functions.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


print("===== SIMPLE CALCULATOR =====")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exit")

while True:
    choice = input("\nChoose an operation (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Please select between 1 and 5.")
        continue

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if choice == "1":
        print("Result =", add(a, b))
    elif choice == "2":
        print("Result =", subtract(a, b))
    elif choice == "3":
        print("Result =", multiply(a, b))
    elif choice == "4":
        print("Result =", divide(a, b))
