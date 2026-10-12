# Program: Find Odd and Even Elements in a List

numbers = [10, 15, 22, 33, 40, 51]

even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]

print("List:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
