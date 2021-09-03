#!/usr/bin/env python3

'''
Реализовать функцию,
принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def division(arg_1, arg_2):
    return(arg_1 / arg_2)

a = int(input('please input number1: '))
b = int(input('please input number2: '))

print(division(a, b))
