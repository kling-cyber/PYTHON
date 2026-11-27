#use of with in file handling
with open("list.txt", "w") as file:
    if file:
     print("File opened successfully")
    else:
     print("Error opening file")
print(file.mode)
#another use of with in file handling
with open("list.txt", "r") as file:
  if file.mode == 'r':
    contents = file.read()
    print(contents)
#or 
file = open("list.txt", "r") as file:
if file.mode == 'r':
    contents = file.read()
    print(contents)
file.close()    
