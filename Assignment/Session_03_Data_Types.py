# TOPS Session 3: Built-in data types and type conversion

age = 20
height_cm = 172.5
name = "Kavish"
has_spotify = True

for value in (age, height_cm, name, has_spotify):
    print(value, "->", type(value))

def total_cart_amount(prices):
    """Convert string prices to floats and return their total."""
    return sum(float(price) for price in prices)

cart_prices = ["199.99", "49", "350.75"]
print("Cart total:", total_cart_amount(cart_prices))

score_text = input("Enter your cricket score: ")
score = int(score_text)
if score >= 50:
    print("Half-century!")
else:
    print("Keep going!")

is_premium = "True"
is_premium_bool = is_premium.strip().lower() == "true"
print(is_premium_bool, type(is_premium_bool))
