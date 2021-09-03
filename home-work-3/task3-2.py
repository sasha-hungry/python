#!/usr/bin/env python3

'''
 Реализовать функцию, принимающую несколько параметров, описывающих 
 данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
 Функция должна принимать параметры как именованные аргументы. 
 Реализовать вывод данных о пользователе одной строкой.
'''

def my_func(name, surname, year_of_birth, sity, email, phone):
	print(f' Имя {name}, Фамилия {surname}, год рождения {year_of_birth}, город проживания {sity}, e-mail {email}, телефон {phone}')

a = input('введите имя: ')
b = input ('введите фамилию: ')
c = input ('введите год рождения: ')
d = input ('введите город проживания: ')
e = input ('введите e-mail: ')
f = input ('введите телефон: ')

my_func (surname = b, name = a, email = e, phone = f, year_of_birth = c, sity = d)
