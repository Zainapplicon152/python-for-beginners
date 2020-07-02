# loops and iterables
# loops are format or code that helps us to repeat iterable or string or any data in multiple time
# two types of loops in python : for and while loop
# iterables => strings are type of iterables , any which we can perform loop are iterables

success = True
for i in range(3):
    print('Attempting!!!')
    if success:
        print("Email sent")
        break
else:
    print("Error")

text = "hello world"
myTuple = ('zain', 'ali', 'malik', 'rehan', 'rehman')
myList = ['zain', 'ali', 'malik', 'rehan', 'rehman']
myDict = [{'name': 'zain'}, {'name': 'ali'}, {'name': 'rehan'}]
mySet = {'zain', 'ali', 'malik', 'rehan', 'rehman'}
myStr = "My name is zain"

for i in myTuple:
    print(i, end=" ")
print('done')

for i in myList:
    print(i, end=" ")
print('done')

for i in mySet:
    print(i, end=" ")
print('done')

for i in myStr:
    print(i, end=" ")
print('done')

for i in myDict:
    print(i['name'], end=" ")
print('done')

for i in text:
    print(i, end=" ")
else:
    print("done")

for i in range(len(text)):
    print(i, end=" ")
print("done")

for i in range(len(text)):
    print(text[i], end=" ")
print("done")

for i in range(5):
    print(i, end=" ")
print("done")

for i in range(1, 5):
    print(i, end=" ")
print("done")
