# input() for use taking input from user

age = int(input("Enter your age: "))
if age >= 22 and age <= 23:
    print("Welcome")
    print("You are allowed")
    print("Thank you!")
    name = input("Enter your name: ")
    if name == 'zain':
        print('welcome zain')
    elif name == 'ali':
        print('Welcome Ali')
else:
    print("You are not allowed")
    print("Good Bye")

# ternary operator
name = input("Enter your name: ")
message = "you are allowed" if name == 'zain' else print('not zain')
print(message)
