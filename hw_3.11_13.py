# Ex.11
import math

def degrees2radians(x):
    ''' Перевод градусов в радианы:'''
    print (degrees2radians.__doc__)
    return math.radians(x)
print('40 =', round(degrees2radians(40),3))
print('45 =', round(degrees2radians(45),3))
print('60 =', round(degrees2radians(60),3))
print('')

# Ex.12

# a)
def sum_of_digits(number):
    '''Сумма 3-х значного числа 324:'''
    print (sum_of_digits.__doc__)
    s = str(number)
    return(int(s[:1]) + int(s[1:2]) + int(s[-1:]))
print('a) =', sum_of_digits(324))

# b)
def sum_of_digits(number):
    n1 = number % 10
    n2 = number % 100 // 10
    n3 = number // 100
    return (n1 +  n2 + n3)
print('b) =', sum_of_digits(324))

# c)
def sum_of_digits(number):
    return sum([int(i) for i in str(number) if int(i)])
print('c) =', sum_of_digits(324))
print('')

# Ex.13

def triangle_square_and_perimeter(a, b):
    '''Площадь треугольника и его периметр:'''
    print (triangle_square_and_perimeter.__doc__)
    c = math.sqrt(a**2 + b**2)
    S = 1 / 2 * a * b
    P = a + b + c
    return (S, round(P,1))
print(triangle_square_and_perimeter(12, 15))


