# 5. Even or Odd

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"


n = int(input("Enter a number: "))
print("The number is", check_even_odd(n))
