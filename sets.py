# like sets in maths
# two method for create sets

mySet1 = {'sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri'}
mySet2 = set('Zain Ul Abideen')
mySet3 = {1, 2, 3, 4, 5, 6, 7, 8}
mySet4 = {1, 22, 9, 4, 53, 66, 7, 8}
myset8 = set()
print(type(myset8))

print(mySet1)
print(mySet2)

mySet5 = mySet3.union(mySet4)
print(mySet5)

mySet6 = mySet3.intersection(mySet4)
print(mySet6)

mySet7 = mySet3.difference(mySet4)
print(mySet7)
