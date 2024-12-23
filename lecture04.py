try:
    x = int(input('x? '))
except ValueError:
    print('error, x not an int')
else: 
    print(f"x is {x}")