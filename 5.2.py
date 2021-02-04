
'''
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

f = open('sth.txt', 'r')
print(f'Содержимое файла:\n{f.read()}')

f = open('sth.txt', 'r')
print(f"Количество строк в документе: {len(f.readlines())}")

f = open('sth.txt', 'r')
lines = f.readlines()
sum = 0
for i in range(len(lines)):
    print(f"Количество элементов в {i + 1}-й строке: {len(lines[i])}\n")
    sum += len(lines[i])
print(f'Общее количество символов во всех строках: {sum}')

f.close()