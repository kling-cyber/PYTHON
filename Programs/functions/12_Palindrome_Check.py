# 12. Palindrome Check

def is_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    return "Not Palindrome"


s = input("Enter a string: ")
print(is_palindrome(s))
