# TOPS Session 2: Python syntax, variables, naming, and comments

# Single-line comment: define a sample order.
item_price = 250
delivery_fee = 30
coupon_discount = 20

print("Item price:", item_price)
print("Delivery fee:", delivery_fee)
print("Coupon discount:", coupon_discount)

# Variable names use snake_case.
team_name = "Gujarat Titans"
runs_scored = 185
overs_played = 20

print(team_name, runs_scored, overs_played)

'''
Multi-line text block / documentation example.
Triple-quoted strings are not a dedicated Python comment syntax.
'''

# Indentation matters in Python.
product_price = 1200
if product_price > 1000:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")
