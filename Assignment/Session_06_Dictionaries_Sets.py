# TOPS Session 6: Dictionaries and sets

# Task 1: Store follower counts for five influencers.
insta_followers = {
    "creator_one": 125000,
    "creator_two": 84000,
    "creator_three": 210000,
    "creator_four": 67000,
    "creator_five": 99000,
}
print(insta_followers)

# Task 2: Add, update, and delete dictionary entries.
insta_followers["creator_six"] = 54000
insta_followers["creator_two"] = 90000
del insta_followers["creator_four"]
print(insta_followers)

# Task 3: Display food items that cost more than ₹200.
food_prices = {
    "pizza": 250,
    "sandwich": 140,
    "thali": 220,
    "pasta": 280,
    "fries": 90,
}
for food, price in food_prices.items():
    if price > 200:
        print(food, price)

# Task 4: Find users with accounts on both platforms.
flipkart_users = {"user_a", "user_b", "user_c", "user_d"}
myntra_users = {"user_c", "user_d", "user_e"}
print(flipkart_users.intersection(myntra_users))

# Task 5: Return unique artists across two playlists.
def get_unique_artists(playlist1, playlist2):
    return set(playlist1).union(set(playlist2))

print(get_unique_artists(["Asha", "Ravi"], ["Ravi", "Mira"]))
