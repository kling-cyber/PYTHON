# TOPS Session 3: Data types and type conversion

# Task 1: Declare variables and display each value and its type.
age = 20
height_cm = 172.5
name = "Your Name"
has_spotify = True

for value in (age, height_cm, name, has_spotify):
    print(value, type(value))

# Task 2: Convert string prices to floats and return the total.
def total_cart_amount(prices):
    return sum(float(price) for price in prices)

print("Cart total:", total_cart_amount(["199.99", "49", "350.75"]))

# Task 3: Convert input text to an integer and check the score.
score = int(input("Enter your cricket score: "))
if score >= 50:
    print("Half-century!")
else:
    print("Keep going!")

# Task 4: Convert a string representation of a boolean correctly.
is_premium = "True"
is_premium_bool = is_premium.strip().lower() == "true"
print(is_premium_bool, type(is_premium_bool))
