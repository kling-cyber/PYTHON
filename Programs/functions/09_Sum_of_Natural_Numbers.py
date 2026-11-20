# 9. Sum of Natural Numbers

def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


n = int(input("Enter a positive integer: "))
if n < 1:
    print("Please enter a positive integer.")
else:
    print("Sum =", sum_natural(n))
