# Program 18: Compound Interest (one-year calculation)

principal = 10000
rate = 5
years = 3

amount = principal * (1 + rate / 100) ** years
compound_interest = amount - principal

print("Final amount:", round(amount, 2))
print("Compound interest:", round(compound_interest, 2))
