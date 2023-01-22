'''
Задание 1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
'''

my_f = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()



'''
Задание 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, 
выполнить подсчёт строк и слов в каждой строке.
'''

with open("file.txt") as f:
    str_list = f.readlines()
for i, string in enumerate(str_list, 1):
    print(f'#{i}: Количество слов: {len(string.split())}')
print(f'Количество строк: {len(str_list)}')



'''
Задание 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину 
их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, 
вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
'''

salary_dict = dict()
try:
    with open('file3.txt') as f:
        salary_list = f.readlines()
    for name in salary_list:
        salary_dict[name.strip().split()[0]] = float(name.strip().split()[1])
        if salary_dict[name.strip().split()[0]] < 20000:
            print(f'{name.strip().split()[0]}: '
                  f'{salary_dict[name.strip().split()[0]]}')
    print(f'Средний доход: {sum(salary_dict.values()) / len(salary_dict):.2f}')
except FileNotFoundError:
    print('Файл не найден')



'''
Задание 4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен 
записываться в новый текстовый файл.
'''

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('file4.txt', 'r', encoding='utf-8') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file4_new.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)



'''
Задание 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''

def summary():
    try:
        with open('file5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода-вывода')
summary()



'''
Задание 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет 
и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество 
занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

FILENAME = "file6_.txt"

subjects = {}

try:
    with open(FILENAME, encoding='utf-8') as fh:
        lines = fh.readlines()

    for line in lines:
        data = line.replace('(', ' ').split()

        subjects[data[0][:-1]] = sum(
            int(i) for i in data if i.isdigit()
        )
except IOError as e:
    print(e)
except ValueError:
    print("Неконсистентные данные")

print(subjects)



'''
Задание 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка 
будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь 
со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''


import json as js

firm_dict = dict()
avg_dict = dict()
f_sum = 0
result_list = []

with open('file7.txt') as raw_file:
    for item in raw_file.readlines():
        firm_dict[item.split()[0]] = int(item.split()[2]) - \
                                     int(item.split()[3])
result_list.append(firm_dict)
for value in firm_dict.values():
    f_sum += value
avg_dict['average_profit'] = f_sum / len(firm_dict)
result_list.append(avg_dict)

with open('file7.json', 'w') as result_file:
    js.dump(result_list, result_file)