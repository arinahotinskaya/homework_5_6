'''
 Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.”
 Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw.
 Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    tittle = None
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        self.tittle = 'ручкой'
        print(f'Запуск отрисовки {self.tittle}')

class Pencil(Stationery):
    def draw(self):
        self.tittle = 'карандашом'
        print(f'Запуск отрисовки {self.tittle}')

class Handle(Stationery):
    def draw(self):
        self.tittle = 'маркером'
        print(f'Запуск отрисовки {self.tittle}')


num_1 = Stationery()

num_2 = Pen()
num_2.draw()

num_3 = Pencil()
num_3.draw()

num_4 = Handle()
num_4.draw()