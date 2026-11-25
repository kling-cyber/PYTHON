# Using logical operators in Python to check login credentials
email = input("Enter your email address: ")
password = input("Enter your password: ")

if email == "admin@gmail.com" and password == "admin":
    print("Login successful!")
else:
    print("Login failed. Please check your email and password.")

# Using a conditional expression in Python to check login credentials
# emailt = input("Enter your email address: ")
# passwordt = input("Enter your password: ")
# print("Login successful!" if emailt == "admin@gmail.com" and passwordt == "admin"
#       else "Login failed. Please check your email and password.")
