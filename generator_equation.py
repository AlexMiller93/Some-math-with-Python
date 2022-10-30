
import random
import math


def generate_numbers():
    """Function generates 3 integer numbers with library random

    Returns:
        _type_: 3 integer numbers
    """
    x = random.randint(-10, 20)
    y = random.randint(-10, 20)
    z = random.randint(-10, 20)
    return x, y, z


def generate_equation():
    """Function generates quadratic equation 
    with random generated numbers 
    and find suitable roots for solving equation 
    between numbers -10 and 10

    Returns:
        _type_: 3 integer numbers 
        which are terms of quadratic equation 
    """
    for x in range(-10, 10):
        while True:
            a, b, c = generate_numbers()
            if a * x ** 2 + b * x + c == 0:
                if a != 0:
                    break

    return a, b, c


def print_equation(a, b, c):
    """_summary_

    Args:
        a (_type_): int number
        b (_type_): int number
        c (_type_): int number
    """
    # some announce
    print('\n** Random math square equation **\n')

    # take 3 int numbers from function
    a, b, c = generate_equation()

    # a cases
    if a == 1:
        print(f'x2 + {b}x + {c}')
    elif a == -1:
        print(f'-x2 + {b}x + {c}')

    # b cases
    elif b == 0:
        print(f'{a}x2 + {c}')
    elif b == 1:
        print(f'{a}x2 + x + {c}')

    # c cases
    elif c == 0:
        print(f'{a}x2 + {b}x')

    else:
        print(f'{a}x2 + {b}x + {c}')

    # printing equation terms
    print(f'a = {a}, b = {b}, c = {c}')


def solve_equation(a, b, c):
    """ Function takes 3 integer numbers 
    and find solutions of quadratic equation

    Args:
        a (_type_): int number
        b (_type_): int number
        c (_type_): int number
    """
    d = b**2-4*a*c  # discriminant

    if d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        print(f"\nThis equation has one solutions:\nx = {x}")
    else:
        x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
        x2 = (-b-math.sqrt(b**2-4*a*c))/2*a

        if int(x1) == x1:
            x1 = int(x1)
        if int(x2) == x2:
            x2 = int(x2)
        print(f"\nThis equation has two solutions:\nx1 = {x1} and x2 = {x2}")


if __name__ == '__main__':
    a, b, c = generate_equation()
    print_equation(a, b, c)
    solve_equation(a, b, c)
