#!/usr/bin/env python3

'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()
'''

from functools import reduce


def multiplication(arg1, arg2):
    return(arg1 * arg2)

input_list = [ element for element in range(100, 1001) if element % 2 == 0]

# вариант со своей функцией
result = reduce(multiplication, input_list)
print(result)

# вариант с lambda
result2 = reduce(lambda a,b: a * b, input_list)

print( 50 * '-')
print( result2 - result)
