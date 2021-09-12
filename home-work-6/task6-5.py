#!/user/loal/bin/python3.7

'''
Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” 
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print('Запуск отрисовки')
        
        
class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Используется {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Будем использовать {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Рисуем на доске, используем {self.title}.')

my_pen = Pen('большая красная ручка')
my_pen.draw()

my_pencil = Pencil('карандаш твердости HB')
my_pencil.draw()

my_handle = Handle('черный маркер')
my_handle.draw()
