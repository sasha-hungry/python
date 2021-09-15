#!/usr/local/bin/python3.7

'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

31  22
37  43
51  86

3  5  32
2  4  6
-1 64 -8

3  5  8  3
8  3  7  1

'''


class Matrix:
    
    def __init__(self, mtrx):
        self.mtrx = mtrx
        
    '''
    def __str__(self):
        row_str = ''
        for row in self.mtrx:
            row_str = row_str + str(row).replace(",", "").strip('[]') + '\n'
        return row_str
    '''
    
    def __str__(self):
        return  '\n'.join(['   '.join([str(row_el) for row_el in row]) for row in self.mtrx ]) + '\n'
          
        '''
        можно через 2 цикла for и перебор каждого элемента, со сборокий строки через \n и пробелы в строках, например:
        row_str = '\n'.join(['   '.join([str(row_el) for row_el in row1]) for row1 in self.mtrx ]) 
        Тут даже можно регулировать расстояние между столбцами, но я через неделю не вспомню как это работает.
        Какой вариант более правильный? 
        '''
        
        
    def __add__(self, add_mtrx):
        result_mtrx = []
        if len(self.mtrx) == len(add_mtrx.mtrx) and len(self.mtrx[0]) == len(add_mtrx.mtrx[0]):
            for row_index in range(len(self.mtrx)):
                for row_el_index in range(len(self.mtrx[row_index])):
                    self.mtrx[row_index][row_el_index] = self.mtrx[row_index][row_el_index] + add_mtrx.mtrx[row_index][row_el_index]
            return Matrix(self.mtrx)            
        else:
            return(' Сложение матриц разного размера невозможно ')
   


mtrx1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
mtrx2 = [[13, 5, 8], [8, 3, 7], [10, -3, -8]]


A = Matrix(mtrx1)
B = Matrix(mtrx2)


print(A)
print(B)


print(A + B )

