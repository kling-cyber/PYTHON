#Using logical operators in Python to check login credentials
email=input("Enter your email address: ")
password=input("Enter your password: ")
if(email=="admin@gmail.com" and password=="admin"):
    print("Login successful!")
else:
    print("Login failed. Please check your email and password.")

#Using ternary operator in Python to check login credentials
#emailt=input("Enter your email address: ")       
#passwordt=input("Enter your password: ")
#(emailt == "admin@gmail.com" and passwordt == "admin") ? print("Login successful!") : print("Login failed. Please check your email and password.")
     
