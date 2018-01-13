
# Ex.15

import math

x1 = 0
y1 = 0
r1 = 4
x2 = 0
y2 = 0
r2 = 4

def circles_intersects(x1, y1, r1, x2, y2, r2):
    a = x2 - x1
    b = y2 - y1
    d = math.sqrt(a**2 + b**2)
    if d >= abs(r1 - r2) or d >= r1 + r2:
        return True
    else:
        return False
print(circles_intersects(x1, y1, r1, x2, y2, r2))