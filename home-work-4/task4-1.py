#!/usr/bin/env python3

'''
 Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv 

def sellary_calc(work_hours, grade, percent_bonus):
    work_hours = int(work_hours)
    grade = int(grade)
    percent_bonus = int(percent_bonus)
    return(work_hours * grade + (percent_bonus / 100) * work_hours * grade)

script_name, work_hours, grade, percent_bonus = argv

sellary = sellary_calc(work_hours, grade, percent_bonus)
print(f'заработная плата: {sellary}')
