#!/usr/bin/env python

a = float(input('введите результат первого дня (a): '))
b = float(input('введите целевой результат (b): ')) 
count = 1

while a < b :
   a = a + a * 0.1
   count = count + 1
   if a >= b :
       break

print(f'На день {count} спортсмен пробежал не менеем {b} километров')


