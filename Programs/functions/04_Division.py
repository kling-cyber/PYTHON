# 4. Division Function

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Division =", divide(a, b))
