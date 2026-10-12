# Program: Find List Elements Greater Than the Average

numbers = [10, 20, 30, 40, 50]

if numbers:
    average = sum(numbers) / len(numbers)
    greater_than_average = [number for number in numbers if number > average]

    print("List:", numbers)
    print("Average:", average)
    print("Elements greater than average:", greater_than_average)
else:
    print("The list is empty.")
