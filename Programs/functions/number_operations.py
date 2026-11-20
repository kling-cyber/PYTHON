# Number Operations
# Find the maximum, minimum, square, or cube using functions.

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c


def find_min(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    return c


def square(n):
    return n * n


def cube(n):
    return n * n * n


print("===== NUMBER OPERATIONS =====")
print("1. Find Maximum (among three numbers)")
print("2. Find Minimum (among three numbers)")
print("3. Find Square")
print("4. Find Cube")
print("5. Exit")

while True:
    choice = input("\nChoose an operation (1-5): ")

    if choice == "5":
        print("Thank you!")
        break

    if choice == "1" or choice == "2":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = float(input("Enter the third number: "))

        if choice == "1":
            print("Maximum number =", find_max(a, b, c))
        else:
            print("Minimum number =", find_min(a, b, c))

    elif choice == "3" or choice == "4":
        n = float(input("Enter a number: "))

        if choice == "3":
            print("Square =", square(n))
        else:
            print("Cube =", cube(n))

    else:
        print("Invalid choice. Please select between 1 and 5.")
