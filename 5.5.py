
'''
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

name_of_new_file = input('Введите название файла, в который хотите занести измененные данные: ')
f = open(name_of_new_file, 'w')
while True:
    try:
        s = input("Введите числа,которые хотите просуммировать. Если хотите выйте, нажмите 'q' : ")
        check = ord(s)
        if check == 81 or check == 113:
            break
        else:
            s = int(s)
            f.write(f'{s}\n')
    except ValueError:
        break

f = open(name_of_new_file, 'r')
file = f.read().split('\n')
file.pop(-1)
print(file)
sum = 0
for i in range(len(file)):
    sum += int(file[i])
print(sum)
f.close()