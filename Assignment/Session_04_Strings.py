# TOPS Session 4: String methods, indexing, slicing, and formatting

product_code = "Flipkart-Sale2024"
clean_code = product_code.lower().replace("-", " ")
print(clean_code)

product_name = " OnePlus Nord-CE 3 "
clean_name = product_name.strip().upper().replace("-", ":")
print(clean_name)

def split_product_code(product_code):
    return product_code.split("-")

print(split_product_code("ZOMATO-FOOD-2024"))

offer = "Spotify_Premium_Offer"
print(offer[7:14])  # Premium

product = "Myntra Shirt"
price = 799.5
print(f"Deal: {product} is available at ₹{price:.2f} only!")
