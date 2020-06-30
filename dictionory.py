# purpose same as tuples and lists
# create with diiferent method and use as different
# we use key value pair for access

myDictionary = {"name": "zain", "age": 22,
                "address": "lahore"}  # "key":"value"    #key value pairs are associative arrays
print(myDictionary["name"])
print(myDictionary.get('age'))

myDictionary2 = [{"name": "zain", "age": 22, "address": "lahore"},
                 {"name": "zaini", "age": 23, "address": "london"},
                 {"name": "zain", "age": 22, "address": "lahore"}
                 ]
print(myDictionary2[0]['name'])

myDictionary.update({"name": "zain malik"})
print(myDictionary)

print(myDictionary.keys())
print(myDictionary.values())
myDictionary.setdefault('isAdmin', False)
print(myDictionary['isAdmin'])

print(myDictionary.items())  # return lists of tuples
