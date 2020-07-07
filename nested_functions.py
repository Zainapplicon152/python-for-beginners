# function inside function
def welcome():
    name = 'zain'

    def greetings(name):
        print(name)

    def bye(name):
        print(name)

    greetings(name)
    bye(name)


welcome()
