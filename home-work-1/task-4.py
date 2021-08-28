#!/usr/bin/env python

temp_list = list(input('введите число; '))
i = len(temp_list)

k = 0
b = 0

while k < i :
    if b <= int(temp_list[k]):
        b = int(temp_list[k])
                
    k = k + 1

print('максимальная цифра в введеном числе;', b)
