def is_even(number):
    '''проверка четности некоторого числа'''
    print (is_even.__doc__)
    return ('Even:', number % 2 == 0)
print (is_even(10))
print (' ')

def is_uneven(number):
    '''проверка не четности некоторого числа'''
    print (is_uneven.__doc__)
    return ('Unven:', number % 2 != 0)
print (is_uneven(11))

