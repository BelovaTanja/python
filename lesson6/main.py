'''
Задание 1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее
сообщение и завершать скрипт.
'''


from time import sleep
from itertools import cycle


class ModificationError(Exception):
    pass


class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный', 'жёлтый']

    def __check_color(self, prev_color, current_color):
        if prev_color in ('красный', 'жёлтый', 'зелёный'):
            if prev_color in ('красный', 'зелёный') \
                    and current_color == 'жёлтый':
                return True
            elif prev_color == 'жёлтый' \
                    and current_color in ('красный', 'зелёный'):
                return True
        elif not prev_color \
                and current_color in ('красный', 'жёлтый', 'зелёный'):
            return True

    def running(self, main_delay=7, cycling_number=10):
        cycling_colors = cycle(self.__color)
        prev_color = ''
        try:
            for i in range(cycling_number):
                current_color = next(cycling_colors)
                if self.__check_color(prev_color, current_color):
                    print(current_color)
                    prev_color = current_color
                    if current_color == 'красный':
                        sleep(main_delay)
                    elif current_color == 'жёлтый':
                        sleep(2)
                    elif current_color == 'зелёный':
                        sleep(main_delay)
                else:
                    raise ModificationError('ModError:  '
                                            'Someone has modified lights...')
        except ModificationError as me:
            print(me)


new_light = TrafficLight()
new_light.running(cycling_number=10)



'''
Задание 2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра 
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''


class Road:
    def __init__(self, road_length, road_width):
        self._length = road_length
        self._width = road_width

    def asphalt_mass(self, asphalt_thickness, sq_m=25):
        return self._width * self._length * asphalt_thickness * sq_m


new_road = Road(5000, 20)
print(f'{new_road.asphalt_mass(5) // 1000} тонн')



'''
Задание 3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода 
с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, вызвать методы экземпляров.
'''

class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


pos1 = Position('Совельева', 'Мария', 'Аналитик', 20000, 3000)
print(pos1.name, pos1.surname, pos1.position)
pos1.get_full_name()
pos1.get_total_income()



'''
Задание 4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, 
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 
40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''

class Car:
    speed = 0
    color = ''
    is_police = False

    def go(self):
        print('Driving...')

    def stop(self):
        print('Stopping...')

    def turn(self, direction):
        print('Turning', direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Speed limit is 60! Your speed is', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Speed limit is 40! Your speed is', self.speed)


class PoliceCar(Car):
    pass


towncar1 = TownCar()
towncar1.speed = 60
towncar1.color = 'red'
towncar1.go()
towncar1.turn('left')
towncar1.stop()
towncar1.show_speed()
print(f'Current speed: {towncar1.speed}, Color: {towncar1.color}\n')

workcar1 = WorkCar()
workcar1.speed = 40
workcar1.color = 'yellow'
workcar1.go()
workcar1.turn('left')
workcar1.stop()
workcar1.show_speed()
print(f'Current speed: {workcar1.speed}, Color: {workcar1.color}\n')

policecar1 = PoliceCar()
policecar1.speed = 90
policecar1.color = 'black'
policecar1.is_police = True
policecar1.go()
policecar1.turn('left')
policecar1.stop()
policecar1.show_speed()
print(f'Current speed: {policecar1.speed}, Color: {policecar1.color}, '
      f'Is it Police: {policecar1.is_police}\n')

sportcar1 = SportCar()
sportcar1.speed = 150
sportcar1.color = 'white'
sportcar1.go()
sportcar1.turn('right')
sportcar1.stop()
sportcar1.show_speed()
print(f'Current speed: {sportcar1.speed}, Color: {sportcar1.color}\n')



'''
Задание 5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить 
уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисую ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисую карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисую маркером')


smth = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

smth.draw()
pen.draw()
pencil.draw()
handle.draw()