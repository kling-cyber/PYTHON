# TOPS Session 4: String methods, splitting, slicing, and formatting

# Task 1
product_code = "Flipkart-Sale2024"
print(product_code.lower().replace("-", " "))

# Task 2
product_name = " OnePlus Nord-CE 3 "
print(product_name.strip().upper().replace("-", ":"))

# Task 3
def split_product_code(product_code):
    return product_code.split("-")

print(split_product_code("ZOMATO-FOOD-2024"))

# Task 4
offer = "Spotify_Premium_Offer"
print(offer[7:14])  # Premium

# Task 5
product = "Myntra Shirt"
price = 799.5
print(f"Deal: {product} is available at ₹{price:.2f} only!")
