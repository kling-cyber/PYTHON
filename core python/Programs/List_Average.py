# Program: Calculate the Average of List Elements

numbers = [10, 20, 30, 40, 50]

if numbers:
    average = sum(numbers) / len(numbers)
    print("List:", numbers)
    print("Average:", average)
else:
    print("The list is empty.")
