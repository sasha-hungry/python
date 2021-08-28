#!/usr/bin/env python

proceeds = input('введите выручку; ')
costs = input('введите издержки: ')

if int(proceeds) > int(costs):
    print('Есть прибыль')
    num = input('колличество сотрудников?; ')
    profit_peer_emploer = (int(proceeds) - int(costs)) / int(num)
    print('прибыль на одного сотрудника: ', profit_peer_emploer)
elif int(proceeds) == int(costs):
    print('похоже ничего не заработали, но и расходов нет')
else: 
    print('Убыток!!!')

