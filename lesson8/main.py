'''
Задание 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Верно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('28 - 1 - 2023')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 11, 2021))
print(Data.extract('08 - 09 - 2011'))
print(today.extract('02 - 03 - 2002'))
print(Data.valid(1, 11, 2010))



'''
Задание 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя 
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''
class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(200, 0))
print(DivisionByNull.divide_by_null(1000, 2))
print(div.divide_by_null(500, 0))



'''
Задание 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие
 только чисел. Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять 
 список необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не 
остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный 
список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
 ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
'''

class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


if __name__ == '__main__':
    my_list = []

    while True:
        user_input = input("Введите число для заполнения списка, или 'stop' для выхода: ")

        if user_input == "stop":
            break

        try:
            if not user_input.isdigit():
                raise NotNumberError(f"'{user_input}' has not numerical format")

            my_list.append(int(user_input))
        except NotNumberError as e:
            print(e)

    print(my_list)




'''
Задание 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные 
типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
 В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
'''
from datetime import datetime

class Depot:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
# внесение в словарь название оборудования, серийный номер и время передачи на склад
        t = datetime.now()
        self.lists.update({equipment.serial_number:[equipment.title, self,t]})
        print('На склад '+self.title+' получено оборудование:'+ '' +equipment.title+' ,серийный номер - '+ str(equipment.serial_number)+', Дата:'
              + str(t.day)+'.'+str(t.month)+'.'+str(t.year))


    def give_to_depot(self, equipment, other):
# передача оборудование на другой склад или подразделение
        t = datetime.now()
        self.give_lists.update({equipment.serial_number: [equipment.title,other, t]})
        print('Передано оборудование:' + '' + equipment.title + ' ,серийный номер - ' + str(
            equipment.serial_number) + ', Дата:'
              + str(t.day) + '.' + str(t.month) + '.' + str(t.year))
        other.take_to_depot(equipment)


    def list_equipments(self):
        print('На склад '+self.title + ' получено оборудование:')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со склада '+self.title + ' выдано оборудование:')
        print(self.give_lists)
        print('Общее количество: ', len(self.give_lists))




class Office_equipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)

class Printer(Office_equipment):
    def __init__(self,title,serial_number, print_velocity):
        Office_equipment.__init__(self,title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.print_velocity)


class Scanner(Office_equipment):
    def __init__(self, title,serial_number,resolution):
        Office_equipment.__init__(self,title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.resolution)

class Copier(Office_equipment):
    def __init__(self, title,serial_number, addit):
        Office_equipment.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.addit)



store1 = Depot('Основной')
store2 = Depot('Малый')
a = Printer('HP',15987,300)
b = Scanner('Epson',3698,15)
c = Copier('Brother',7845, 600)
d = Printer('HP',9878,5000)

print(a)
print(b)
print(c)

store1.take_to_depot(a)
store1.take_to_depot(b)
store1.take_to_depot(c)
store1.take_to_depot(d)

store1.give_to_depot(a,store2)

store1.list_equipments()
store2.list_equipments()



'''
Задание 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники 
на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве 
единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
'''

class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorageError(StorageError):
    def __init__(self, text):
        self.text = f"отсутствует возможность добавить товар на склад:\n {text}"


class TransferStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Ошибка при передаче оборудования:\n {text}"


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} не является оргтехникой")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Недопустимый тип '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"


class OfficeEquipment:
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('xerox', *args)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer("HP", "L805"))
    storage.add(Scanner("Acer", "AD-457"))
    storage.add(Xerox("Xerox", "F123"))
    print(storage)

    last_idx = None
    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)
        last_idx = idx

    print("Передаем 1 устройство")
    storage.transfer(last_idx, 'Отдел ЯФ')

    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)

    print(storage)
    print("Удаляем 1 устройство")
    del storage[last_idx]
    print(storage)


'''
Задание 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках 
по ООП.
'''
class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AcceptStorageError(AppError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferStorageError(AppError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


AddStorageError = AcceptStorageError


class ValidateEquipmentError(AppError):
    pass


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddStorageError(f"Вы пытаетесь добавить на склад не оргтехнику")

        self.__storage.extend(equipments)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Недопустимый тип '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"


class OfficeEquipment:
    __required_props = ("eq_type", "vendor", "model")

    def __init__(self, eq_type: str = None, vendor: str = "", model: str = ""):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' должен иметь значение отличное от false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; количество инстансов должен быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Xerox', **kwargs)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer.create(4, vendor="Epson", model="XP-400"))
    storage.add(Scanner.create(3, vendor="OKI", model="5367-AD"))
    storage.add(Scanner.create(2, vendor="OKI", model="5368-AD"))
    storage.add(Xerox.create(6, vendor="Xerox", model="F123"))
    print(storage)

    for idx, itm in storage.filter_by(department=None, vendor="OKI", model="5367-AD"):
        print(f"Резервируем {itm} в 'Отдел ЯФ'")
        storage.transfer(idx, 'Отдел ЯФ')

    for idx, itm in storage.filter_by(department=None):
        print(idx, f"{itm} не распределены по отделам")

    print(storage)
    print("Списываем 1 устройство")
    del storage[0]
    print(storage)






'''
Задание 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. 
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных 
экземпляров. Проверьте корректность полученного результата.
'''

class MyComplex:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex + other
        return MyComplex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex * other
        return MyComplex(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


if __name__ == '__main__':
    c1 = MyComplex(2, -3)
    c2 = MyComplex(5)

    print(c1 + c2, complex(2, -3) + complex(5))
    print(c1 * c2, complex(2, -3) * complex(5))
