#!/usr/local/bin/python3.7

'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''

class Warehouse:
    
    def __init__(self):
        self.storage = dic()


class OfficeEq:
    
     def __init__(self, name, price):
         self.name = name
         self.price = price
         


class Printer(OfficeEq):
    
    def __init__(self, name, price, color, type_priter):
        self.name = name
        self.price = price
        self.color = color
        self.type_priter = type_priter

class Scan(OfficeEq):
    
    def __init__(self, name, price, color, size):
        self.name = name
        self.price = price
        self.color = color
        self.size = size


class Copier(OfficeEq):
    
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size


my_printer = Printer('HP', 1000, True, 'laser')
print(my_printer.__dict__)
     
     
