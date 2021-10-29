#!/usr/local/bin/python3.7

'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
'''

class ComplexNum:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        result_a = self.a + other.a
        result_b = self.b + other.b
        return ComplexNum(result_a, result_b)
    
    def __mul__(self, other):
        result_a = self.a * other.a - self.b * other.b
        result_b = self.a * other.b + self.b * other.a
        return ComplexNum(result_a, result_b)
    
    def __str__(self):
        return(f'{self.a} + {self.b}*i')   

z1 = ComplexNum(2, 4)
z2 = ComplexNum(3, 2)
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
