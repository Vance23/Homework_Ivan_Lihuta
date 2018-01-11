# но ведь по нижеуказанном варианте 1 так и происходит: при значении = 10 возвращает True, при = 11 - False, т.е. условие выполняется?

#Вариант решения 1 
# вставляем 10, выдает True
def is_even(number):
    return (number % 2 == 0)
print (is_even(10))

# вставляем 11, выдает False
def is_even(number):
    return (number % 2 == 0)
print (is_even(11))
print (' ')

# Вариант решения 2 (пока не разобрался как это привести в одну строку, буду еще пробывать) 
def is_even(x):False
    if x % 2 == 0:
        return True
    else:
        return False
print (is_even(10))
