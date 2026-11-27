#rename a file
import os
try:
    os.rename("list.txt", "new-list.txt")
    print("File renamed successfully.")
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to rename this file.")