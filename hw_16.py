import math

v1 = 50
v2 = 60
def have_trains_crashed(v1, v2):
    s = 10
    s1 = 4
    t1 = (s1 / v1)
    t2 = ((s - s1) / v2)
    return t1 >= t2
print(have_trains_crashed(v1, v2))