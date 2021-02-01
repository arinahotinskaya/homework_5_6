'''
Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
Необходимо написать программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

rus = {'One' : 'Один',
       'Two' : 'Два',
       'Three' : 'Три',
       'Four' : 'Четыре'}

new = []

f = open('numbers.txt', 'r')
lines = f.read().split('\n')
count = len(lines)

with open('numbers.txt', 'r') as dig:
    for i in dig:
        i = i.split(' ', 2)
        new.append(rus[i[0]] + ' : ' + i[2])
    print(new)


name_of_new_file = input('Введите название файла, в который хоите занести измененные данные: ')
f = open(name_of_new_file, 'w')
f.writelines(new)






