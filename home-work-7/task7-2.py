#!/usr/local/bin/python3.7

'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: 
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

'''

from abc import ABC, abstractmethod

class MyAbstractClothes(ABC):

    @abstractmethod
    def __init__(self, metric):
        pass
       
        
    @abstractmethod
    def calc(self):
        pass

class Clothes(MyAbstractClothes):
    
    def __init__(self, metric):
        self.metric = metric
    
    def calc(self):
        pass

class Coat(Clothes):
   
    @property
    def calc(self):
        return self.metric / 6.5 + 0.5

class Suit(Clothes):
        
    @property
    def calc(self):
        return self.metric * 2 + 0.3

        
my_coat = Coat(15)
my_suit = Suit(10)

total_cloth = my_coat.calc + my_suit.calc

print(f'общий раскод ткани {total_cloth} метров погонных')
