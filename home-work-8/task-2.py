#!/usr/local/bin/python3.7

'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class MyExceptionDivisionZerro(Exception):
    '''
    def __init__(self, a, b):
        self.a = a
        self.b = b
    '''
    @staticmethod
    def my_div(a,b):
        try:
            return(a / b)
        except ZeroDivisionError:
            print('на ноль делить нельзя')
            return None

         
a = int(input('введите делимое: '))
b = int(input('введите делитель: '))
print(MyExceptionDivisionZerro.my_div(a,b))        
    
    
