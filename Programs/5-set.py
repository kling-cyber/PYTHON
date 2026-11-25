# A set is used to store multiple values in a single variable
# A set stores unique elements (duplicate values are removed)
# A set is unordered (elements do not have fixed positions)
# A set is mutable (elements can be added or removed)
# A set does not support indexing or slicing
# A set is enclosed between {}
# A set can also be defined using the set() constructor


# declaration of set

# set1={10,20,30,40}
# set2={"brijesh","kavish","noorie"}
# set3={10,"python",20.5,True}

# print(set1)
# print(set2)
# print(set3)
# print(type(set1))


# set using constructor

# set1=set([10,20,30,40])
# print(set1)
# print(type(set1))


# empty set

# set1=set()
# print(set1)
# print(type(set1))


# duplicate values in set

# set1={10,20,20,30,30,40}
# print(set1)


# add elements in set

# set1={10,20,30}
# set1.add(40)
# print(set1)

# set1.update([50,60])
# print(set1)


# remove elements from set

# set1={10,20,30,40}
# set1.remove(20)
# print(set1)

# set1.discard(30)
# print(set1)

# res=set1.pop()
# print(res)
# print(set1)

# set1.clear()
# print(set1)


# set operations

# a={1,2,3,4}
# b={3,4,5,6}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))


# iterate a set

# set1={"brijesh","kavish","noorie"}
# for i in set1:
#     print(i)


# live example

student={"brijesh","kavish","noorie","jay"}

print(student)
print(type(student))

student.add("amit")
print(student)

for i in student:
    print(i)
