# 8. Multiplication Table

def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


n = int(input("Enter a number: "))
table(n)
