#!/usr/bin/env python3

'''
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

'''


def my_func(arg1, arg2):
    arg2 = abs(arg2)
    return( 1 / (arg1 ** arg2))



def my_func2(arg1, arg2):
    arg2 = abs(arg2)
    i = 1
    tmp_result = arg1
    while i < arg2 :
      tmp_result = tmp_result * arg1
      i += 1
    return(1 / tmp_result )
    
    
a = int(input('введите первое число: '))
b = int(input('введите второе отрицательное число: '))
print(my_func(a, b))
print(50 * '-')
print(my_func2(a, b))
