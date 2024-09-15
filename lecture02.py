print("shutup")

score = int(input('score here: '))

if score > 100:
    print('error')
elif score >= 90:
    print('a')
elif score >= 80:
    print('b')
elif score >= 70:
    print('c')
elif score >= 65:
    print('d')
else:
    print('f')



x = int(input("x "))
y = int(input("y "))

if x < y: 
    print("x<y")
elif x > y:
    print("x>y")
else:
    print("x==y")

if x < y or x > y:
    print('x!=y')
else:
    print('x==y')


def is_even(n):
    return True if x % 2 == 0 else False

print(is_even(3))

match 'H': 
    case 'H':
        print('bad')
    case 'Y' | 'O' | 'U': 
        print('good')
    case 'N':
        print('other')
    case _:
        print('_')
