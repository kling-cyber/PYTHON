#define a file 
#read
file = open("list.txt","r")
if file:
    print("File opened successfully")
else:
    print("Error opening file")
print(file.mode)
file.close()
#write
file = open("list.txt","w")
if file:
    print("File opened successfully")
else:
    print("Error opening file")
print(file.mode)
file.close()


