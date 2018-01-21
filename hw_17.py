import math

# квадратное уравнение (ax**2 + bx + c = 0)
# d - дискриминант

a = 10
b = 2
c = 0

def solve_quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    print(d)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return(x1, x2)
    elif d == 0:
        x1 = -b / (2 / a)
        x2 = None
        return (x1, x2)
    else:
        x1 = None
        x2 = None
        return(x1, x2)

print(solve_quadratic_equation(a, b, c))