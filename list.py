#list
#list used to store data in single variable in squencial order
#tuple performance fast from lists
#lists are dynamic or changable not as tuple

myList = [1 , 2 , 3 , 4]
myList2 = ['sat' , 'sun' , 'mon' , 'tue']

print(myList2)
print(myList2[0])

print(myList2.count('sat'))
print(myList2.index('sun'))

myList2.append(1)
print(myList2)

del(myList2[4])
print(myList2)

ml = myList2.pop(0)
print(ml)

myList2.append('thu')
print(myList2)

myList2.insert(3 , 'wed')
print(myList2)

