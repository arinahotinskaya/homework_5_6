'''
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина под названием {self.name} поехала')

    def stop(self):
        print(f'Машина под названием {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина под названием {self.name} повернула {self.direction}')

    def show_speed(self):
        print(f'Машина имеет скорость {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превышаете скорость на {self.speed - 60}. Сбавьте!')
        else:
            print(f'У вас нормальная скорость!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превышаете скорость на {self.speed - 40}. Сбавьте!')
        else:
            print(f'У вас нормальная скорость!')

class PoliceCar(Car):
    pass

town = TownCar(90, 'зеленый', 'BMW')
town.go()
town.show_speed()
town.turn("направо")
town.stop()
print('\n')

sport = SportCar(110, 'белый', 'Maserati')
sport.go()
sport.show_speed()
sport.turn("налево")
sport.stop()
print('\n')

work = WorkCar(50, 'серый', 'WAZ')
work.go()
work.show_speed()
work.turn("назад")
work.stop()
print('\n')

police = PoliceCar(80, 'белый', 'Mercedes-Benz', True)
police.go()
police.show_speed()
police.turn("направо")
police.stop()