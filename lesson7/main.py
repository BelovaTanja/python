'''
Задание 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, matrix_list):
        self.matrix = matrix_list

    def __str__(self):
        result_output = ''
        for line in self.matrix:
            result_output += ''.join(str(line)) + '\n'
        return result_output

    def __add__(self, other):
        if (len(self.matrix[0]) != len(other.matrix[0])) \
                or len(self.matrix) != len(other.matrix):
            print('Have to be equal size matrices')
        else:
            result_matrix = []
            row = []
            for line in zip(self.matrix, other.matrix):
                for i, item in enumerate(line[0]):
                    row.append(item + line[1][i])
                result_matrix.append(row)
                row = []
            return result_matrix


mtx_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mtx_list2 = [[5, 9, 1], [8, 23, 7], [1, 1, 9]]

mtx1 = Matrix(mtx_list1)
mtx2 = Matrix(mtx_list2)
print(mtx1)
print(mtx2)
mtx3 = Matrix(mtx1 + mtx2)
print(mtx3)



'''
Задание 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, name=None):
        self.name = name

    @abstractmethod
    def material(self):
        pass


class Coat(Clothes):
    def __init__(self, size, name=None):
        super().__init__(name)
        self.V = size

    @property
    def material(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height, name=None):
        super().__init__(name)
        self.H = height

    @property
    def material(self):
        return self.H * 2 + 0.3


suit = Suit(15)
print(suit.material)
coat = Coat(20)
print(f'{coat.material:.2f}')



'''
Задание 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. 
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, 
соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы 
методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), 
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к 
клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) 
деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме 
ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек 
двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение 
количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное 
деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно 
переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются 
все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() 
вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() 
вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
'''

class Cell:
    def __init__(self, parts):
        self.parts = int(parts)
        self.__i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i <= self.parts:
            return self.__i
        else:
            raise StopIteration

    def __add__(self, other):
        self.parts += other.parts
        self.make_order(5)

    def __sub__(self, other):
        sub_result = self.parts - other.parts
        if sub_result > 0:
            self.parts = sub_result
            self.make_order(5)
        else:
            print('Less than zero')

    def __mul__(self, other):
        self.parts *= other.parts
        self.make_order(5)

    def __truediv__(self, other):
        self.parts = round(self.parts / other.parts)
        self.make_order(5)

    def make_order(self, parts_number):
        i = 0
        while i < self.parts // parts_number:
            print('*' * parts_number + '\n', end='')
            i += 1
        print('*' * (self.parts % parts_number))


cell1 = Cell(10)
cell2 = Cell(12)

# Testing
cell1 + cell2
print('=' * 10)
cell1 - cell2
print('=' * 10)
cell1 * cell2
print('=' * 10)
cell1 / cell2
print('-' * 10)
cell2.make_order(3)

[print(item, end=' ') for item in cell2]