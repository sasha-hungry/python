#!/user/loal/bin/python3.7

'''
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

with open('my_text_file.txt', 'w') as my_f:
    while True:
        input_string = input('введите строку: ')
        if len(input_string) != 0:
            my_f.write(input_string +'\n')
        else:
            break
    
