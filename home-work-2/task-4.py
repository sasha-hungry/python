#!/usr/bin/env python

'''
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''

my_input_string = input('введите несколько слов; ').split()

# enumerate  - https://docs.python.org/3/library/functions.html#enumerate 

for i, world in enumerate(my_input_string, start=1) : 
    print (i , world[:10])
   


