
'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый)
— 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''

from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while True:
            if i == 3:
                i = 0
            if i == 0:
                print(f'На светофоре: {self.__color[i]}')
                sleep(7)
            elif i == 1:
                print(f'На светофоре: {self.__color[i]}')
                sleep(2)
            elif i == 2:
                print(f'На светофоре: {self.__color[i]}')
                sleep(7)
            i += 1

now = TrafficLight()
now.running()