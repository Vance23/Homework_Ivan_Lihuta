
# Ex.7
               #0123456789
current_date = '05.17.2016'
month = str(current_date[0:2])
day = str(current_date[3:5])
year = str(current_date[6:10])
point = '.'
current_date1 = str(day + point + month + point + year)
print(current_date1)

# Ex.8

name = 'Mark Zukerberg'
name.split(' ')
name_1st = name.split(' ')
tabl = ' '
print(name_1st[1] + tabl + name_1st[0])


#Ex. 9 (В Питоне 3.6 появились: f'' строки, которые разрешают произвольные выражения в формате: s = 'aBc def'; print(f'{s.title()}') --> Abc Def)

s = 'employee_ivan_lihuta'
s0 =(f'{s.title()}')
# Можно оставить  '_' и вывести как было только с заглавными буквами
print(s0)
# Можно убрать '_' через добаление еще одной переменной используя сплит
s1 = s0.split('_')
print(s1[0] + s1[1] + s1[2])



# Ex.10

writer = 'Leo Tolstoy*1828-08-28*1910-11-20'

# вариант решения 1

writer1 = str(writer[0:11])
date_of_birth = str(writer[12:16])
date_of_death = str(writer[23:27])
age = int(date_of_death) - int(date_of_birth)
print (writer1 + ',' + str(age))

# вариант решения 2

writer2 = writer.split('*')
birth = ((writer2[1])[0:4])
death = ((writer2[2])[0:4])
age1 = int(death) - int(birth)
print(writer2[0] + ',' + str(age1))

# (остался вопрос: можно ли используя сплит включать два разделителя * и -, у меня неполучилось)
