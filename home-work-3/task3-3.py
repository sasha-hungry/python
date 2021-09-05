#!/usr/bin/env python3

'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        sum_max_arg = arg1 + arg2
    elif arg1 >= arg2 and arg3 >= arg2:
        sum_max_arg = arg1 + arg3
    else: 
        sum_max_arg = arg2 + arg3
    return(sum_max_arg)

a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
c = int(input('введите третье число: '))

print(my_func(a, b, c))

