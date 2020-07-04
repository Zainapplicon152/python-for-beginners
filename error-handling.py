x = input('>')
while x.lower() != 'quit':
    try:
        print(eval(x))
    except NameError:
        print(f"name '{x}' is not defined")
    except SyntaxError as Error:
        print(Error)
    finally:
        x = input('>')

try:
    x = int(input('Enter a number: '))
    y = int(input('Enter another number: '))
    print(x / y)
except ValueError as error:
    print('invalid literal for int()')
except ZeroDivisionError:
    print('Division by zero is not allowed')
finally:
    x = int(input('Enter a number: '))
    y = int(input('Enter another number: '))
    print(x / y)
