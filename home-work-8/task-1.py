#!/usr/local/bin/python3.7

'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год 
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, 
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

class Data:
    def __init__(self, data):
        self.data = data
    
    @classmethod
    def convertor(cls, data):
        day, month, year = map(int, data.split('-'))
        return day, month, year
    
    @staticmethod
    def inputs_check(data):
        day, month, year = Data.convertor(data)
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 99:
                    return( 'формат даты верный')
                else:
                    return('ошибка формата года')
            else:
                return('ошибка формата месяца')
        else:
            return('ошибка формата дня')
     
    

data = input('введите дату dd-mm-yy: ')
print(Data.convertor(data))
print(Data.inputs_check(data))
