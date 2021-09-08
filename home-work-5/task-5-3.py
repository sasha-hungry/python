#!/user/loal/bin/python3.7

'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
тест файла:

Ложкин 30000
Чашкин 25000
Поворешкина 45000
Скалкин 12000
Черпалкин 25000
Вилкина 30000
Блюдцев 18000
Тарелкин 45000


'''

surname_salary = dict()
with open('my_file_task3.txt','r') as my_f:
    for line in my_f:
        input_list = line.split()
        surname_salary[input_list[0]] = input_list[1]
        

i = 1
count = 0
for  surname, salary in surname_salary.items():
    j = int(salary)
    count = count + j
    i += 1
    if int(salary) < 20000:
        print(f'сотрудник {surname} имеет зарплату меньше 20k')
        
      
print(f'средняя зарплата {count / i:.8}')
        
