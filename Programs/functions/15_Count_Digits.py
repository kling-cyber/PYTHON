# 20. Count Digits

def count_digits(n):
    n = abs(n)

    if n == 0:
        return 1

    count = 0
    while n > 0:
        count += 1
        n //= 10

    return count


n = int(input("Enter an integer: "))
print("Total digits =", count_digits(n))
