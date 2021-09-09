#!/user/loal/bin/python3.7

'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

'''
translate = { '1':'Один',  '2':'Два', '3':'Три', '4':'Четыре' }

in_f = open('my_file_task4_input.txt','r')
out_f = open('my_file_task4_out.txt', 'w')

for line in in_f:
    in_list = line.split()
    print(translate[in_list[2]], ' - ', in_list[2], file = out_f)
   
in_f.close()
out_f.close()




