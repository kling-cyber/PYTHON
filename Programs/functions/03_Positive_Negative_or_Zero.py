# 6. Positive, Negative or Zero

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"


n = float(input("Enter a number: "))
print("The number is", check_number(n))
