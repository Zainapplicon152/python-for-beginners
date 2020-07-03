# nested loops
text = "hello world"
myTuple = ('zain', 'ali', 'malik', 'rehan', 'rehman')
myList = ['zain', 'ali', 'malik', 'rehan', 'rehman']
myDict = [{'name': 'zain'}, {'name': 'ali'}, {'name': 'rehan'}]
mySet = {'zain', 'ali', 'malik', 'rehan', 'rehman'}
myStr = "My name is zain"
count = 1
for i in range(3):
    for j in range(3):
        for k in range(3):
            # print(i, j, k)
            print(f"({count} i:{i} , j:{j} , k:{k})")
            count = count + 1

myDict2 = {"name": "imran", "age": 40,
           "address": {'city': 'lahore', 'country': 'pakistan', 'map': {'lat': 2.333, 'lng': '3.333'}}}
for i in myDict2:
    print(myDict2[i])
print(myDict2['address']['city'])
print(myDict2['address']['country'])

for i in myDict2:
    if isinstance(myDict2[i] , (dict)):
        for j in myDict2[i]:
            print(f"{j}:{myDict2[i][j]}", end=" ")
        else:
            print(f"{i}:{myDict2[i]}" , end=" ")
