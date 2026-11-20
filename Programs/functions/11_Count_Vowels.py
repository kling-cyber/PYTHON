# 16. Count Vowels

def count_vowels(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count += 1
    return count


s = input("Enter a string: ")
print("Total vowels =", count_vowels(s))
