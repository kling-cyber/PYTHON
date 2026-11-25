# A list is used to store multiple values in a single variable
# A list is ordered (elements maintain their position)
# A list provides mutable elements (can be changed)
# A list can store duplicate values
# A list is enclosed between []
# A list can store different data types
# A list can also be defined using the list() constructor


# declaration of list

# list1=[10,20,30,40]
# list2=["brijesh","kavish","noorie"]
# list3=[10,"python",20.5,True]

# print(list1)
# print(list2)
# print(list3)
# print(type(list1))


# list using constructor

# list1=list((10,20,30,40))
# print(list1)
# print(type(list1))


# accessing list elements

# list1=[10,20,30,40,50]
# print(list1[0])
# print(list1[1])
# print(list1[-1])


# slicing of list

# list1=[10,20,30,40,50]
# print(list1[::1])
# print(list1[::-1])
# print(list1[0:3])
# print(list1[1:4])
# print(list1[0:-2])


# update data in list

# list1=[10,20,30,40]
# list1[1]=25
# print(list1)


# add elements in list

# list1=[10,20,30]
# list1.append(40)
# print(list1)

# list1.insert(1,15)
# print(list1)

# list1.extend([50,60])
# print(list1)


# remove elements from list

# list1=[10,20,30,40,50]
# list1.remove(30)
# print(list1)

# res=list1.pop()
# print(res)
# print(list1)

# list1.clear()
# print(list1)


# list method

# list1=[10,20,30,20,40]

# res=list1.count(20)
# print(res)

# res=list1.index(30)
# print(res)

# list1.sort()
# print(list1)

# list1.reverse()
# print(list1)

# res=list1.copy()
# print(res)


# iterate a list

# list1=["brijesh","kavish","noorie"]
# for i in list1:
#     print(i)


# live example

student=["brijesh","kavish","noorie","jay"]
marks=[85,90,78,88]

print(student)
print(type(student))

print(marks)
print(type(marks))

print(student[0])
print(student[1])

student.append("amit")
marks.append(92)

print(student)
print(marks)

for i in student:
    print(i)
