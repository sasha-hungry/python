#!/user/loal/bin/python3.7

'''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json


out_dict = dict()
profit_dict = {'average_profit':0}
count_firms = 0
sum_profit =0

with open('my_file_task7.txt') as my_in_f:
    for line in my_in_f:
        in_list = line.split()
        proceeds = int(in_list[2])
        costs = int(in_list[3])
        profit = int(in_list[2]) - int(in_list[3])
        if profit >= 0:
            sum_profit = sum_profit + profit
            count_firms += 1  # в среднюю прибыль учитываются фирмы с прибылью больше нуля
        out_dict[in_list[0]] = profit
        
profit_dict['average_profit'] = sum_profit / count_firms
out_list = ( out_dict, profit_dict)
print(out_list)

with open('my_file_task7.json','w') as my_out_f:
    json.dump(out_list, my_out_f)
