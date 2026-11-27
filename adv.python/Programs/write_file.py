#write in file
#write
file = open("list.txt","w") 
if file:
    print("File opened successfully")
    txt1 = "This is a test file.\n"
    txt2 = "This file is used to test file operations.\n"
    file.write(txt1)
    file.write(txt2)
    print(file.write(txt1))
    print(file.write(txt2))
else:
    print("Error opening file")
print(file.mode)
file.close()
#read
file = open("list.txt","r")
if file:
    print("File opened successfully")
else:
    print("Error opening file")
print(file.mode)
file.close()

