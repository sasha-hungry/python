#!/usr/bin/env python3

'''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''

def int_func(arg1):
    '''
    arg1 is string
    '''
        
    return(arg1.capitalize())



def my_func(arg2):
    '''
    arg2 is string
    '''
    input_list = arg2.split()
    out_list = list()
    for el in input_list:
        el = int_func(el)
        out_list.append(el)
    return(' '.join(out_list))
    



word = input('введите слово: ')
print(int_func(word))

input_string = input('введите строку: ')
print(my_func(input_string))
