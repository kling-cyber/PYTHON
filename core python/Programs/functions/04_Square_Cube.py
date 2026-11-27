# Square and Cube
# Find the square or cube of a number using functions.

def square(n):
    return n * n


def cube(n):
    return n * n * n


print("===== SQUARE AND CUBE =====")
print("1. Find Square")
print("2. Find Cube")
print("3. Exit")

while True:
    choice = input("\nChoose an operation (1-3): ")

    if choice == "3":
        print("Thank you!")
        break
    elif choice == "1" or choice == "2":
        n = float(input("Enter a number: "))

        if choice == "1":
            print("Square =", square(n))
        else:
            print("Cube =", cube(n))
    else:
        print("Invalid choice. Please select between 1 and 3.")
