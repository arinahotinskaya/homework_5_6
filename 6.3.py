'''
 Реализовать базовый класс Worker (работник),
 в котором определить атрибуты: name, surname, position (должность), income (доход).
 Последний атрибут должен быть защищенным и ссылаться на словарь,
 содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
 Создать класс Position (должность) на базе класса Worker.
 В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
 и дохода с учетом премии (get_total_income).
 Проверить работу примера на реальных данных (создать экземпляры класса Position,
 передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
    name = None
    surname = None
    position = None
    income__ = None

class Position(Worker):
    def get_full_name(self):
        name = input()
        surname = input()

    def get_total_income(self):
        