#!/user/loal/bin/python3.7


'''
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''


i = 1
count = dict()
with open('my_file_task2.txt','r') as my_f:
    for line in my_f:
        count[i] = len(line.split())
        i += 1

        
        
print( f'кол-во строк: {i - 1}')

print ('кол-во слов в каждой строке в формате № строки: кол-во слов \n' )
print (count)

'''
my_f = open('my_file_task2.txt','r')
for line in my_f:
    print(line)
'''

        
        
