# TOPS Session 6: Dictionary and set practice

insta_followers = {
    "creator_one": 125000,
    "creator_two": 84000,
    "creator_three": 210000,
    "creator_four": 67000,
    "creator_five": 99000,
}
print(insta_followers)

# Add a creator and update an existing follower count.
insta_followers["creator_six"] = 54000
insta_followers["creator_two"] = 90000

# Delete a creator.
del insta_followers["creator_four"]
print("Updated followers:", insta_followers)

food_prices = {
    "pizza": 250,
    "sandwich": 140,
    "thali": 220,
    "pasta": 280,
    "fries": 90,
}
print("Food items costing more than ₹200:")
for food, price in food_prices.items():
    if price > 200:
        print(food, price)

flipkart_users = {"user_a", "user_b", "user_c", "user_d"}
myntra_users = {"user_c", "user_d", "user_e"}
print("Users on both platforms:", flipkart_users.intersection(myntra_users))

def get_unique_artists(playlist1, playlist2):
    return set(playlist1).union(set(playlist2))

print(get_unique_artists(["Asha", "Ravi"], ["Ravi", "Mira"]))
