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
    
    storage = dict()
    
    def __init__(self):
        pass
        
    def income(self, position, items):
        self.position = position
        self.items = items
        self.storage[self.position] = items
        return self.storage
        


class OfficeEq:
    
     def __init__(self, name, price):
         self.name = name
         self.price = price
         


class Printer(OfficeEq):
    
    def __init__(self, name, price, color, type_printer):
        self.name = name
        self.price = price
        self.color = color
        self.type_printer = type_printer
    
    def validate(self, name, price, color, type_printer):
        if type(self.price) == int:
            if type(self.color) == bool:
                items = { 'name':self.name, 'price':self.price, 'color':self.color, 'type_printer': type_printer }
                return items
            else:
                print('color должен принимать значения True или False')
                return None
        else:
            print('цена должна быть цифрой')
            return None
           

class Scan(OfficeEq):
    
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color
        
    def validate(self, name, price, color):
        if type(self.price) == int:
            if type(self.color) == bool:
                items = { 'name':self.name, 'price':self.price, 'color':self.color }
                return items
            else:
                print('color должен принимать значения True или False')
                return None
        else:
            print('цена должна быть цифрой')
            return None



class Copier(OfficeEq):
    
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size
        
    def validate(self, name, price, size):
        if type(self.price) == int:
            items = { 'name':self.name, 'price':self.price, 'size':self.size }
            return items
        else:
            print('цена должна быть цифрой')
            return None


my_printer = Printer('HP', 1000, True, 'laser')
my_scaner = Scan('HP',500, True)
my_copier = Copier('Xerox', 2000, 'A3')

# print(type(my_printer), my_printer.__dict__)
# print(my_printer.validate('HP', 1000, True, 'laser'))

my_warehouse = Warehouse()

my_warehouse.income('printers', my_printer.validate('HP', 1000, True, 'laser'))
my_warehouse.income('scaners', my_scaner.validate('HP', 500, True))
my_warehouse.income('copier', my_copier.validate('Xerox', 2000, 'A3'))
