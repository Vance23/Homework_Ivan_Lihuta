def is_even(number):
    '''проверка четности некоторого числа'''
    print (is_even.__doc__)
    if number % 2 == 0:
        return True
    else:
        return False
print (is_even(11))
print (is_even(10))
print (' ')

def is_even(number):
    '''проверка не четности некоторого числа'''
    print (is_even.__doc__)
    if number % 2 != 0:
        return True
    else:
        return False
print (is_even(11))
print (is_even(10))