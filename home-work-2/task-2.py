#!/usr/bin/env python

'''
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input()
'''

my_input_list = list(input('введите элементы последоватеьно; '))

print(my_input_list)

for k in range(0, len(my_input_list) - 1, 2):
    my_input_list[k], my_input_list[k + 1] = my_input_list[k + 1], my_input_list[k]

print(my_input_list)


