# A tuple is used to store multiple values in a single variable
# A tuple is ordered (elements maintain their position)
# A tuple provides immutable elements (can not be changed)
# A tuple can store duplicate values
# A tuple is enclosed between ()
# A tuple can store different data types
# A tuple can also be defined using the tuple() constructor


# declaration of tuple

# tuple1=(10,20,30,40)
# tuple2=("brijesh","kavish","noorie")
# tuple3=(10,"python",20.5,True)

# print(tuple1)
# print(tuple2)
# print(tuple3)
# print(type(tuple1))


# tuple using constructor

# tuple1=tuple([10,20,30,40])
# print(tuple1)
# print(type(tuple1))


# accessing tuple elements

# tuple1=(10,20,30,40,50)
# print(tuple1[0])
# print(tuple1[1])
# print(tuple1[-1])


# slicing of tuple

# tuple1=(10,20,30,40,50)
# print(tuple1[::1])
# print(tuple1[::-1])
# print(tuple1[0:3])
# print(tuple1[1:4])
# print(tuple1[0:-2])


# tuple methods

# tuple1=(10,20,30,20,40)

# res=tuple1.count(20)
# print(res)

# res=tuple1.index(30)
# print(res)


# iterate a tuple

# tuple1=("brijesh","kavish","noorie")
# for i in tuple1:
#     print(i)


# single element tuple

# tuple1=(10,)
# print(tuple1)
# print(type(tuple1))


# live example

student=("brijesh","kavish","noorie","jay")
marks=(85,90,78,88)

print(student)
print(type(student))

print(marks)
print(type(marks))

print(student[0])
print(student[1])

for i in student:
    print(i)
