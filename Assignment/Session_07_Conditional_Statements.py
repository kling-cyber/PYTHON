# TOPS Session 7: Conditional statements

listening_minutes = int(input("Enter your Spotify listening time in minutes: "))
if listening_minutes > 120:
    print("You are a true music fan!")
else:
    print("Keep listening!")

order_amount = float(input("Enter your Zomato order amount: "))
if order_amount > 300:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")

cart_total = float(input("Enter your Flipkart cart total: "))
if cart_total > 2000:
    print("You get a 10% discount")
elif cart_total > 1000:
    print("You get a 5% discount")
else:
    print("No discount available")

team_points = int(input("Enter your IPL fantasy team points: "))
if team_points > 800:
    print("Champion")
elif team_points >= 500:
    print("Top Performer")
else:
    print("Keep Trying")

# Ternary expression example from the README operators section.
status = "Adult" if team_points >= 18 else "Minor"
print("Ternary example:", status)
