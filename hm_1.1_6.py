import math

a = 6
b = 3
c = 4

# Ex.1
x1 = a + b * (c / 2)
print(x1)

# Ex.2
x2 = ((a**2 + b**2) % 2)
print(x2)

# Ex.3
x3 = (a + b) / 12 * c % 4 + b
print(x3)

# Ex.4
x4 = (a - b * c) / (a + b) % c
print(x4)

# Ex.5
x5 =  abs(a - b) / (a + b)**3 - math.cos(c)
print(x5)

# Ex.6
x6 = (math.log(1 + c) / - b)**4 + abs(a)
print(x6)
