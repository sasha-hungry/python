#!/usr/bin/env python3

'''
Реализовать функцию,
принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def division(arg_1, arg_2):
    if int(arg_2) == 0:
        return('на ноль делить нельзя')
    else:
        return(int(arg_1) / int(arg_2))

a = input('please input number1: ')
b = input('please input number2: ')

print(division(a, b))
