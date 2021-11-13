#!/usr/bin/env python3

'''
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24
'''

def my_fact(arg):
    result = 1
    for i in range(1, arg + 1):
        result = result * i
        yield result 

n = int(input('введите число до которого создавать список из факториалов: '))

for el in my_fact(n):
    print(el)



