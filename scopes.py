# scope
name = 'zain'  # global variable # will be use anywhhere in this file


def greetings():
    print(name)


greetings()

num = 100  # global scope


def check():
    if (num > 100):
        print(f"{num} is greaten than hundred")
    else:
        print(f"{num} not bigger than hundred")


check()


def zain():
    name = 'malik'  # local scope
    print(name)


zain()

message = 'welcome'


def welcome():
    global message
    print(message)
    message = 'Good bye'
    print(message)


welcome()
print(message)
