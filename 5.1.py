'''
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''


my_file = input('Enter name of file: ')
f = open(my_file, 'w')
print(type(f))
while True:
    s = input("Enter sth in file: ")
    if s == '1':
        break
    f.write(f'{s}\n')
f.close()