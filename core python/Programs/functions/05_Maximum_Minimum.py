# Maximum and Minimum
# Find the largest or smallest among three numbers using functions.

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


print("===== MAXIMUM AND MINIMUM =====")
print("1. Find Maximum")
print("2. Find Minimum")
print("3. Exit")

while True:
    choice = input("\nChoose an operation (1-3): ")

    if choice == "3":
        print("Thank you!")
        break
    elif choice == "1" or choice == "2":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = float(input("Enter the third number: "))

        if choice == "1":
            print("Maximum number =", find_max(a, b, c))
        else:
            print("Minimum number =", find_min(a, b, c))
    else:
        print("Invalid choice. Please select between 1 and 3.")
