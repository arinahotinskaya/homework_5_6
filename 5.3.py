'''
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

f = open('работники.txt', 'r')
print(f'Содержимое файла:\n{f.read()}')

f = open('работники.txt', 'r')
count = len(f.readlines())
print(f'{count}')

f = open('работники.txt', 'r')
normal = f.read().split('\n')
bad = []
okay = []
digits = []
for i in normal:
    i = i.split()
    if int(i[2]) < 20:
        bad.append(i[0])
        digits.append(int(i[2]))
    else:
        okay.append(i[0])
        digits.append(int(i[2]))

print(f'Фамилии тех, кто имеет оклад менее 20 тысяч рублей: {bad}')
print(f'Средняя величина дохода сотрудников: {round(sum(digits) / count, 3)} тысяч')