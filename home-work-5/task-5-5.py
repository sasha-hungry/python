#!/user/loal/bin/python3.7

'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randint

with open('my_file_task5.txt','w+') as my_f:
    out_list = [str(randint(1,100)) for i in range(randint(15,30))]
    out_string = ' '.join(out_list)
    my_f.write(out_string)
    my_f.seek(0)
    input_string = my_f.read()
    my_sum = 0 
    for i in input_string.split():
        my_sum += int(i)
    

print(f'сумма числел в файле {my_sum}.')
    

