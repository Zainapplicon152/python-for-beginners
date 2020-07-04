# collection of blocks or code that we will call anywhere for some specfic task is called a function
# defining function
def my_func():
    print("hello")  # return none


# calling a function
print(my_func())


# function with argument
# argument : jb function define kro us k sath diye jatay hain
# parameter : jb argument functions ki calling k doran pass kiye jay

def arg_function(name, age):  # passing arguments
    print(f"Welcome, {name} your age is, {age}")
    return 0  # return userdefined value


print(arg_function('zain', 22))  # passing parameters


# types of functions
# two types of functions in function
# return none or user defined value

def add(num1, num2):
    return num1 + num2  # return userdefined value


result = add(5, 5)
print(result)

# keyword arguments
arg_function(name='zain', age=22)  # dont know wht is 22 #so from this we know wht is 22


# defualt arguments
def default_arg(gender="male"):  # default value in  function defining #default arguments are always write on end but with keyword args
    return gender


print(default_arg())
