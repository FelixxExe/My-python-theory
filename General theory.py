#----------------------------------Для начала работы с пайтон----------------------------------

'''
	Наличие пайтон
Чтобы проверить наличие пайтон на винде, нужно зайти в терминал(Windows PowerShell)
после написать команду: python --version

	Установка пайтон
Сайт - https://www.python.org/downloads/
Выбрать свою операционную систему
Если на виндовс, то ставим галочку Add python.exe to PATH во время инсталяции

	Установка Visual Studio Code
сайт - https://code.visualstudio.com/
Выбрать свою операционную систему
Обязательно в самой программе добавить расширение code runner и рекомендуемые программой
Расширение для русского языка - Russian Language Pack for Visual Studio Code
'''

#----------------------------------Работа с консолью, команды----------------------------------

'''
# Сайт всех существующих модулей: https://pypi.org/

pip list - выведет все сторонние установленные пакеты для данной версии пайтон
pip install <название пакета> - установка стороннего пакета для данной версии пайтон
pip install <название пакета>==<версия> - установка стороннего пакета с его версией для данной версии пайтон
pip install -r <текстовый файл> - установка сторонних пакетов с текстового файла для данной версии пайтон
pip freeze > <название файла>.txt - создаст файл с данным названием, где будут названия модулей и их версий для данной версии пайтон
'''

#----------------------------------Работа с print()----------------------------------
'''
\n - перенос строки (воспринимается, как один символ)
\t - одна табуляция (воспринимается, как один символ)
\ + любой символ = этот символ (воспринимается, как один символ) (экранирование)

r"" - сырая строка (в ней игнорируются все спец. символы) (raw-строки)

конкатенация - соединение строк (+)

end="" - что в конце
sep="" - чем разделять
'''

#----------------------------------Способы записи чисел----------------------------------

'''
5e2 - равносильно записи 5 * 10**2
8e-100 - равносильно записи 8 * 10**(-100)

1101 = 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0 = 13 - способ перевода из двоичной в десятиричную систему счисления
FB = F*16^1 + B*16^0 = 251 - способ перевода из шестнадцатиричной в десятиричную систему счисления
27 = 2*8^1 + 7*8^0 = 23 - способ перевода из восьмиричной в десятиричную систему счисления

0b001 - способ записи доичного числа (0b + двоичное число) (чтобы сделать отрицательным,добавляем унарный минус)
0x1A - способ записи шестнадцатиричного числа (0x + шестнадцатиричное число) (чтобы сделать отрицательным,добавляем унарный минус)
0o27 - способ записи шестнадцатиричного числа (0o + восьмиричное число) (чтобы сделать отрицательным,добавляем унарный минус)

1_000_000_000 - можно записать так число и это будет корректно
'''

#----------------------------------О переменных----------------------------------

'''
a = 7
ссылка = объект
переманная а ссылается на объект 7

тип переменной определяется в момент присваивания (динамическая типизация)

a = 4
b = a
a и b ссылаются на один объект 4

a = b = c = 0 # каскадное прискаивание (при каскадном присваивании все переменные ссылаются на один объект)
a, b = 9, 5 # множественное присваивание

с = None # переменная с ничем или пустая

a = 5
a = -a

del a # удаление переменной (можно использовать для удаление всего)
'''

#----------------------------------Полезные встроенные функции----------------------------------

'''
bin() - возвращает указанное число в двоичной записи
round() - округление к ближайшему целому (второй аргумент - до скольки округлять)
id() - возвращает индификатор объекта, на который ссылается переменная
type() - возвращает тип данных указанной переменной
abs() - модуль указанного числа
pow() - возведение указанного числа в указанную степень
ord() - принимает один символ и возвращает код символа из ASCII
chr() - обратное ord()
enumerate() - возвращает индекс и значение
all() - вернёт тру, если все тру
any() - вернёт тру, если хотя бы один тру
help() - вернет описание в заданной функции
iter() - с помощью этой вункции можно получить итератор
next() - для перебора итерируемых объектов
map() - первый аргумент - имя функции, второй - итерируемый объект. Применяет данную функцию к каждому элементу итерируемого объекта
filter() - первый аргумент - имя функции, второй - итерируемый объект. Если функция возвращает тру, то filter возвращает значение итерируемого объекта, на котором велась проверка
zip() - минимум два аргумента, которые являются итерируемыми объектами. Создает кортежи из элементов итерируемых обектов, пока один из них не закончится
isinstance() - первый аргумент - объект, второй - тип данных (можно указать несколько в кортеже). Если объект соответствует указанному типу данных, то вернёт тру с учётом наследования


# Примеры

#             ENUMERATE
lst = [56, 1234, 125, 5132, 1, 24, 4]
for i, n in enumerate(lst): # i - индекс значения, n - ссылка на значение
	print(i, n)

#             MAP
# Вовращает итератор, который можно перебирать с помощью next()
# Её использую в замену генератору для удобства
# Дважды по этой функции пройтись нельзя
a = map(int, ['1', '2', '3', '4', '5'])
или можно так
a = (int(x) fpr x in ['1', '2', '3', '4', '5'])

#             FILTER
# Возвращает итератор, который можно перебрать с помощью next()
# Можно сделать вложенновсть функций filter

#             ZIP
# Можно распределять по переменным, если известно количество:
# a = [1, 2, 3, 4]; b = [5, 6, 7, 8, 9, 0]; c = "python"; z1, z2, z3, z4 = zip(a, b, c)
#
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 0]
c = "python"
z = zip(a, b, c)
for i in z:
	print(i) # (1, 5, 'p') (2, 6, 'y') (3, 7, 't') (4, 8, 'h')

#             ISINSTANCE
print(isinstance(True, int)) # вернет тру, так как тип bool наследуется от int
'''

#----------------------------------Полезные методы----------------------------------

'''
.copy() # копирует элементы
.__sizeof__() # возвтращает размер в байтах в памяти указанного элемента
.__name__() # возвращает имя функции
.__doc__() # возвращает описание функции
'''

#----------------------------------Списки (list)----------------------------------

'''
p = [i for i in range(10)] # Однострочный список

c = [1, 2, 3, 4, [5, 6]]
print(c[-1][1])
c.append('eee') # добавить элемент в конец списка
c.insert(1, "value") # добавить элемент в список по индексу и остальное смещается
c.index() # вернёт индекс первого найденного указанного значения. Второй аргумент - с какого индекса начинать поиск
c.reverse() # разворачивает список
c.extend([444, 333, 555]) # добавить в конец списка ряд элементов
c.pop(0) # укажешь индекс - удалит по индексу, нет - удалит последний
c.remove(4) # удалит элемент с указанным значением
c[-1].remove(6)
c.sort() # сортировка списка по возрастанию (меняет сам список), но можно вторым аргументом прописать reverse=True и отсортирует по убыванию.
 Сортирует только списки. Есть аргумент key, в которм можно указать фукцию и она будет применяться к каждому элементы раньше самой сортировки.
sorted(c) # возвращает список отсортированных по возрастанию элементов, но можно вторым аргументом прописать reverse=True и отсортирует по убыванию.
 Можно сортировать всё. Есть аргумент key, в которм можно указать фукцию и она будет применяться к каждому элементы раньше самой сортировки.
c.clear() # удалит всё
print(c)

d = [1, 2, 3, 4, 5, 6, 7, [8, 9]]
print(*d)

lst = [1, 2, 3, 4]
lst2 = lst[:] # копия списка lst
'''

#----------------------------------Строки----------------------------------

'''
# строка - неизменяемый объект
# "hello {0}, i\'m funny {1}".format(name1, name2) - подставит по индексам в строке соответствующие переменные (можно добавить ключи к переменным и указывать их)
w = "qRweRrRty"
q = None
w.upper() # всё к верхнему регистру
w.lower() # всё к нижнему регистру
w.isupper() # возвращает тру если вся строка в верхнем регистре
w.islower() # возвращает тру если вся строка в нижнем регистре
w.capitalize() # каждый первый символ к верхнему регистру
w.find("er") # возвращает индекс элемента. Можно указать с какого считать и каким заканчивать счёт(не включительно заканчивать). Вернёт -1, если не найдёт
w.rfind("er") # то же, что и .find(), но начинает с конца
w.count("R") # возвращает количество указанных символов в строке. Можно указать с какого считать и каким заканчивать счёт(не включительно заканчивать)
w.index() # вернёт индекс указанной строки
w.isalpha() # вернет тру, если вся строка состоит из букв
w.isdigit() # вернет тру, если вся строка состоит из цифр
w.rjust(20, "0") # первый аргумент - до скольки удленить строку, второй аргумент - чем удленить(по умолчанию пробел; добавит слева; только один символ)
w.ljust() # то же, что и .rjust(), только добавит справа
w.strip() # удаляет все пробелы и переносы строк в начале и в конце строки. Есть .rstrip() - удалит справа и .lstrip() - удалит слева
q = w.split("R") # разбивает строку на список с разделением в виде указанного(ых) символа(ов)

s = ["eee", "rrr", "ttt"]
res = "|".join(s) # превращает список в строку, где элементы этого списка разделены указанным символом
print(res)
'''

#----------------------------------F-строки----------------------------------

'''
# Не важен регистр при написании буквы "f"
# Можно написать f-сторуку так: f"{a=}", где a - некая переменная. В выводе будет: название переменной = её значение
# a = 10
# print(f"{a=}")
# Можно написать: f"{value:.1f}" и тогда выведет переменную с одним числом после запятой
# value = 3.56
# print(f"{value:.5f}") # Вывод: 3.56000
'''

#----------------------------------Срезы----------------------------------

'''
# с какого индекса (по умолчанию 0) : до какого индекса (по умолчанию до конца) : с каким шагом (по умолчанию 1)
# всё не включительно
# подходит и для строк, и для списков

w = [1, 23, 4, 5, 6, 7, 8, 9]
print(w[::])
w[1:3] = [123, 122]
print(w)
'''

#----------------------------------Кортежи (tuple)----------------------------------

'''
# Работают срезы
# Нельзя менять (добавлять, удалять и т.д.), но можно брать
# Можно объединять кортежи с помощью "+". Например: a = () + (1,) или a += (1,) или a = (1, 2) + (4,)
# Работает .count(), len(), .index(), in
# Кортеж из одного элемента: data = (5,) или data = 5,
# Копия не создастся если написать a = b[:] - a ссылается на b
# Можно изменить внутри кортежа список, например
a = 1, 2, 3 # кортеж создан
a = a * 10

x, y = (1, 2)
x, y = [1, 2]
x, y = "12"

p = tuple(i for i in range(10)) # Однострочный кортеж (?)
'''

#----------------------------------Словари (dict)----------------------------------

'''
# {ключ: значение, ключ: значение, ключ: значение}
# dict(one=1, two=2)
# Словарь - это неупорядоченная коллекция
# в качестве ключа нельзя использовать списки, но можно кортежи. Значение - любое
# Т.е. в качестве ключа только неизменяемые типы данных
# вывод: print(d["b"]) => 2

p = {str(i): i**2 for i in range(10)} # Однострочный словарь

d = {"a": 1, "b": 2, True: 3, "d": 4, "f": 5}
d2 = dict(a=1, b=2, c=3, d=4, f=5)

# d.keys() # создаёт список из ключей словаря
# d.values() # создаёт список из значений словаря
# d.items() # превращает словарь в список с кортежами ключ и значение этого словаря
# d.get("a") # то же, что и d["a"]
# d.clear() # очищает словарь
# d.pop("f") # удаляет элемент по ключу. Второй аргумент - то, что возвращать, если ключ несуществует
# d.popitem() # удаляет последний элемент
# del d["a"] # удаляет элемент по ключу
d["d"] = "123" # обновит значение или создаст новый ключ:значение
# работает len()
# "asd" in d - проверка наличия ключа

# lst = [1, 2, 3, 4, 5, 6]
# a = dict.fromkeys(lst) # Создаёт значения по заданному ключу. Второй аргумент - сами ключи
# print(a)
# Вывод: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None}

# d.setdefault()

# d = {1: None, 2: None, 3: None,}
# d2 = {4: True, 2: True, 6: True,}
# d.update(d2) # совпадающие ключи перезаписываются, другие - добавляются

# d3 = {**d, **d2} # объединение словарей
# d3 = **d | **d2 # объединение словарей

# for key, value in d.items():
# 	print(key, value)

# for key in d:
# 	print(key) # вывод ключей
# 	print(d[key]) # вывод значений
'''

#----------------------------------Множества (set, frozenset)----------------------------------

'''
# все элементы в случайном порядке и нет повторяющихся
# нельзя обращаться к элементам по индексам и менять элементы
# во множестве только неизменяемые типы данных
# можно идалять и добавлять элементы
# frozenset - неизменяемое множество
# & - операция пересечения (возвращает новое множество), | - оператор объединения(возвращает новое множество)

p = {i for i in range(10)} # Однострочное множество

a = set() # только так можно создать пустое множество
data = set("972324") 
data = {1, 2, 2, 3, 3, 4, 5, 3, 3, 3}

data.add(32) # добавляет во множество указанный элемент
data.update(["54", True, 444]) # добавляет несколько указанных элементов во множество
data.remove(3) # удаляет указанный элемент
data.discard(2) # удаляет из множества указанный элемент и, при попытке удалить несуществующий объект, ошибки не будет
data.pop() # удаляет "первый" элемент
data.clear() # очищает множество

frset = frozenset([9, 7, 2, 3, 2, 4])

print(frset)

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}

print(setA & setB) # выведет пересечение этих множеств (3, 4), т.е. общее для них
# альтернатива для &: setA.intersection(setB)
# альтернатива с сохранением в первом указанном (setA): setA.intersection_update(setB)

print(setA | setB) # выведет объединение этих множеств (1, 2, 3, 4, 5, 6, 7)
# альтернатива для |: setA.union(setB)

# вычитание множеств
print(setA - setB) # вывод: {1, 2}
print(setB - setA) # вывод: {5, 6, 7}

# симетричная разность - уникальные элементы
print(setA ^ setB) # вывод: {1, 2, 5, 6, 7}

'''

#----------------------------------Функции----------------------------------

'''
# Имя функции - ссылка на обект-функцию
# () - оператор вызова функции
# Допустимо: f = print
# Рекомендуется называть функции в виде глагола
# def func(a, b, c, d=True, f=False) - a, b, c - фактические параметры, d, f - формальные парамтры
# Позиционные аргументы идут в начале, а именованные в конце: func(1, c=2, b=3)
# *args - произвольное количество позиционных аргументов (создает кортеж)
# **kwargs - произвольное количество именованных аргументов (создает словарь, где ключи - имена аргументов и значения - значения аргументов)
# def func(a, *args, d=True, **kwargs)

a = lambda x, y: x + y
a(1, 2)
'''

#----------------------------------Операторы * и ** упаковки и распаковки----------------------------------

'''
# Упаковка
x, *y = (1, 2, 3, 4, 5, 6) # первое значенив в x, остальные в y (y - список из остальных значений)

# Распаковка
a = [1, 2, 3, 4]
b = (*a,) # тоже самое, но кортеж

c = -5, 5
print(list(range(*c)))

d = {"a": 1, "b": 2, True: 3, "d": 4, "f": 5}
d2 = dict(a=1, b=2, c=3, d=4, f=5)
print({**d, **d2}) # единый словарь
'''

#----------------------------------Области видимости переменных, global, nonlocal----------------------------------

'''
# Функция имеет свою локальную область
# global - делает переменную глобальной
# nonlocal - выводит переменную из данной области видимости в следующую локальную

# n = 100
# w = 12
# def f(a): 
# 	global n, w
# 	n = 20
# 	w = 30
# 	return a + n + w
# print(f(1), n, w)

x = 0
def f1():
	x = 1
	def f2():
		nonlocal x
		x = 2
		print("f2:", x)
	f2()
	print("f1:", x)
f1()
print("global:", x)
'''

#----------------------------------Работа с файлами----------------------------------

'''
# open(file, mode="r", encoding=None) - путь к файлу, режим открытия, кодировка
# mode по умолчанию равер "r"
# "../file.txt" - две точки - это выход из данного каталога или обратиться к родительскому каталогу
# Обязательно закрывать, чтобы не было утечки памяти
# Если файла по ссылке несуществует, то он будет создан (если на запись или на добавление)

# w (как write) - режим для записи, r (как read) - режим для чтения, a (как append) - режим добавление
# w - стирает, что было, и записывает новое (переписать файл)
# r - чтает файл (прочесть файл)
# a - добавляет к тому, что есть (добавить в файл)
# Так же есть "a+" - добавлять и считывать
# В кодировке utf-8 есть невидимый символ в начале и конце

# Есть еще: "wb" - на запись в бинарном режиме, "rb" - на чтение в бинарном режиме
# Для всего жтого нужно импортировать библиотеку pickle
# Файл должен быть с расширением .bin
# В ней есть pickle.dump(books, file), где первый аргумент - сами данные, вотрой - сам файл
# Так же есть pickle.load(file), где первый аргумент - сам файл (возвращает)


# f = open("SomeFile.txt", "w")
# f.write("qwerty\n") # запишет в файл, что задали
# f.writelines(['1', '2', '3']) # добавляет в файл всё, что в указанном списке
# f.close() # закрытие файла


# f = open("SomeFile.txt", "r")
# f.read(0) # если нет аргумента, то возвращает весь текст файла, если есть(в формате int), то выедет указанное количество символов
# f.seek(0) # можно управлять файловой позицией
# f.tell() # возвращать номер байта текущей файловой позицией
# f.readline() # возвращает первую строку файла
# f.readlines() # возвращает список из строк файла (применять для маленьких файлов)
# f.close()


# Менеджер контекста
with open("SomeFile.txt", "r") as fileForTest: # удобно использовать with ... as:, так как не нужно самому закрывать файл
	print(fileForTest.read())
'''

#----------------------------------Обработка исключений (try, except, else, finally)----------------------------------

'''
# try: - тут пишем то, что обрабатываем
# except название ошибки: - запускается если возникла ошибка при обработке
# else: - запускается, если try сработал корректно
# finally: - всегда запускается после try или except
# Если один из except сработал первее, то остальные игнорируются
# Можно написать в одном except несколько ошибок, переданных в кортеже
# Если хоти отлавливать все ошибки в однос except, то пишем except:

a = 0
while a == 0:
	try:
		a = int(input())
		a = 5 / a
		print(a)
	except ValueError:
		print("error")
	except ZeroDivisionError as z:
		print(z)
	else:
		print("Great! It's working!")
	finally:
		print("Hey, I'm working all the time!")


# Видимую ошибку в консоли можно назвать иначе - исключение
# Каждое исключение имеет своё название и текст об ошибке
# Исключения бывают разный видов и типов
# Ошибки возникающие в процессе выполнения программы - исключения в момент исполнения
# Синтаксические ошибки - исключения при компиляции (до исполнения кода)
# Обработка исключений происходит при первом типе (в момент выполнения)
# После обработки исключения программа продолжит работать, если except написаны верно

# У исключений есть своя иерархия
# Зная её, мы можем писать except, учитывая наследование

# Можно написать except ValueError as v: где v - ссылка на экземпляр класса ValueError

# Если обрабатывать исключения в функции, то return сработает после обработки
# Можно делать вложенную обработку

# Можно самим генерировать исключения с помощью raise
# Например: raise TypeError("Error") # Вывод: TypeError: Error
# Принято основываться на классе Exception при создании своих исключений
# Можно создать свой класс исключений, унаследовав от Exception, и использовать его
# Желательно написать описание к такому классу о нём
# Так же можно прописать функционал. Нпример: __init__ __str__ и др.
'''

#----------------------------------Битовые операции И, ИЛИ, НЕ, XOR, >>, <<----------------------------------

'''
a = 5
b = 4

print(~a) # битовое НЕ. Число уменьшилось на один

print(a & b) # битовое И. Пример:
#  5:  0 0 0 0 0 1 0 1
#  4:  0 0 0 0 0 1 0 0
# 5&4: 0 0 0 0 0 1 0 0 = 4
# Можно проверить включен ли бит или выключить определённые биты числа (res = a & ~ b)

print(a | b) # битовое ИЛИ
# Применяют когда нужно включить отдельные биты переменной

print(a ^ b) # исключающее ИЛИ или XOR
# Удобно переключать биты и используется для шифрования информации

# Преоритеты по убыванию: ~, &, (| и ^)

a = 160
print(bin(a))
print(bin(a >> 1)) # сдвиг вправо
# если >> 1 то равнократно // 2, а если >> 2 - равнократно // 4
# как два в степени
print(bin(a))
print(bin(a << 1)) # сдвиг влево
# если << 1 то равнократно * 2, а если >> 2 - равнократно * 4

# >> и << работают быстрее чем * и //
'''

#----------------------------------Замыкания----------------------------------

'''
def f1(a=" "):
	def f2(st):
		return st.strip(a)
	return f2
s = f1()
print(s("  131 23 "))
'''

#----------------------------------Декораторы----------------------------------

'''
import webbrowser as wb

url = "https://ya.ru/"

def validator(func):
	def wrapper(url):
		#print("Before") # то, что работает до выполнения функции openURL
		if "." in url:
			func(url) # сама функция
		else:
			print("Error")
		#print("After") # то, что работает после выполнения функции openURL
	return wrapper

@validator
def openURL(url): # просто открывает сайт по указанной ссылке
	wb.open(url)

# Можно создать много дополнительных функций и не нужно повторяться
# Можно добавить несколько декораторов

openURL(url)


def f1(func): # универсальный декоратор для любых функций
	def f2(*args, **kwargs): # для универсальности добавили *args и **kwargs
		print("здесь всё до вызова функции")
		res = func(*args, **kwargs) # для универсальности добавили *args и **kwargs
		print("здесь всё после вызова функции")
		return res # для универсальности добавили return и res
	return f2

def some_func():
	print("вызов функции some_func")

f = f1(some_func)
f()
# Или
some_func = f1(some_func) # равносильно @f1 перед нужной функцией (используют такой способ)
some_func()



def f1(a=True): # синтаксис декоратора с параметром
	def f2(func):
		def f3(*args, **kwargs):
			if a:
				res = func(*args, **kwargs)
				return res
			else:
				print("nonono")
		return f3
	return f2

@f1(1)
def s_f(x):
	print(f"x = {x}")

s_f(100)
'''

#----------------------------------Выражения генераторы, функция-генератор, оператор yield----------------------------------

'''
# В генераторах списков, словарей, множеств числа генерируются с помощью конструкции: next() + генератор
# Можно определить сам генератор без привязки к какой-либо коллекции:
# a = (x**2 for x in range(6)) - это именно генератор, а не кортеж
# Генераторы можно перебирать с помощью next(a) или for x in a: print(x)
# Перебор генераторов можно осуществить только один раз
# Можно использовать некоторые функции на генераторах: list, set, sum, max, min и др.
# Нельзя использовать функции: len
# Нельзя обращаться по индексу
# Генераторы не хранять все значения в памяти, а генерируют их при необходимости


def get_list(): # пример функции-генератора (функция с yield)
	for i in [1, 2, 3, 4]:
		yield i # возвращает текущее значение и замораживает состояние функции до следующего вызова
a = get_list() # a ссылается на некий объект-генератор
for i in a:
	print(i)


# Пример работы и применения такой функции
def find_word(f, w):
	g_indx = 0
	for line in f:
		indx = 0
		while indx != -1:
			indx = line.find(w, indx)
			if indx > -1:
				yield g_indx + indx
				indx += 1
		g_indx += len(line)

try:
	with open("SomeFile.txt") as fl:
		a = find_word(fl, "rt")
		print(list(a))
except FileNotFoundError:
	print("FileNotFoundError")
except:
	print("Error")
'''

#----------------------------------Аннотация типов----------------------------------

'''
# <название переменной>: <тип данных>
# Аннотация типов нужна для упрощения читаемости кода, удобства редоктирования, отслеживания ошибок. Она не влияет ни на что
# Пример: a: int = 10; b: float = 1.2; c: bool = True и так далее со всеми типами
# Среда подскажет методы (атрибуты), если будет аннотация типов

# def func1(x: int | float, y: bool = True) -> int: # возвращает int, принимая int или float и bool
# 	return x**2 if y else x

# def func2(x: str, y: bool = True) -> None: # возвращает None, принимая str и bool
# 	print(x*2 if y else x)

# print(func1.__annotations__) # выведет словарь параметрами и их типами


#from typing import Union, Optional, Any, Final, Callable
# Union[int, bool, ...] - объединение нескольких типов в один тип. Пример: a: Union[int, bool] или int | bool (с версии 3.10)
# Optional[int] - можно написать только один тип данных и автоматически будет добавлен тип None. Пример: a: Optional[int]
# Any - любой тип данных. Пример: a: Any
# Final - константа (нельзя менять). Пример: a: Final = 100
# Callable[[int, str], None] - в скобках - типы параметров функции, второе - тот тип, который функция вернёт. Пример: a: Callable[[], int]
# Можно создать переменную с сыллкой на эти штуки


# Коллекции так же, но с особенностями (можно без указания типа внутри)
# lst: list[int] = [1, 2, 3] - в скобках тот тип, который имеют все элементы списка
# tpl: tuple[int, str, bool] = [1, "py", True] - в скобках нужно прописать тип для каждого элемента кортежа. Но если хочется один для всех, то пишем tuple[int, ...]
# dct: dict[str, int] = {"1": 1, "2": 2, "2": 3} - в скобках первое - тип данных для ключей, второе - для значений
# st: set[int] = {1, 2, 3} - в скобках тот тип, который имеют все элементы множества


# Все стандартные тивы данных наследуются от класса object
# Классы - тоже своего рода типы данных и их можно использовать

class Geom: pass
class Line(Geom): pass

g: Geom = 100
g = Line() # тоже справедливо, так как наследуется

# Тип Any совместим с любым другим типом, а тип object - ни с каким другим
# Другими словами: тип Any - любой тип (может подстраиваться под необходимый), а тип object - это тип object
# К object можно присвоить любой тип, но сам object не присвоить к другим типам
a: Any = None
s: str 

s = a # справедливо с типом Any, но не справедливо с типом object


# Есть специальный модуль для проверки аннотаций: mypy
# Пишем в консоли mypy <название рабочего файла> и проверит всё на корректность (?)
...

'''
#----------------------------------Конструкция match/case----------------------------------

'''
# На версии 3.10+
# В match указываем переменную для проверки, а в case шаблон проверки
# Если хоть один case срабатывает, то сразу же после выполнения кода в нем происходит выход из match
# В case обязательно должен быть шаблон и содержаться хоть какой-то код
# В match обязательно должен быть минимум онид case
# Движение сверху внизу и слева на право
# Следует сначала писать более частные случаи
# Можно комбенировать match/case и if/elif/else
# Переменные можно использовать в дальнейшем коде (match работает в глобальной области видимости)
# Если мы хотим использовать константы в case, то можно импортом или создавать константы в классе

# cmd = "qwerty"

# match cmd:
# 	case "top":
# 		print("moving top")
# 	case "right" | "left": # или это, или то
# 		print("moving right or left")
# 	case command: # значение "cmd" присваевается новой переменной "command" 
# 		print(f"another command: {command}")
# 		# Желательно писать в конце, так как срабатывает всегда


# cmd = [1, 2, 3, 4]

# match cmd:
# 	case str() as st if len(st) > 2: # проверка на тип str с присваиванием и проверкой на длину большую двух
# 		# сначала проверка на тип, потом присваивание, проверка условия (или guard (защитник))
# 		print(f"it's string: {st}. It's > 2")
# 	case str(): # проверка на тип str
# 		# можно указать допю тип: str() | list()
# 		print("it's srting")
# 	case int() as item: # проверка на тип int с присваиванием переменной "item" 
# 		print(f"it's int: {item}")
# 		# можно иначе записать: int(item)
# 		# переменная создаётся после проверки на тип
# 		# проверка на тип подобна функции isinstance(), то есть с учётом наследования
# 		# лучше проверку на bool писать раньше проверки на int из-за ^
# 	case _: # wildcard. Работает если ни один другой case не сработал
# 		print("not correctly")


# cmd = (1, 2, 3, 4)

# match cmd:
# 	case dict():
# 		print("I don't need your dict!!")
# 	case int() as a, b, c: # распоковка, если ровно из трех элементов c проверкой первого элемента на тип int
# 		print(f"it's: {a, b, c}")
# 		# может распоковать и кортежи, и списки
# 	case (_, a, b, c, *_) if len(cmd) < 10 and len(cmd) > 5:
# 		print(f"it's: {a, b, c}")
# 		# скобки могут быть квадратные и круглые, и они ничего не значат(только для визуала)
# 	case tuple() as tpl:
# 		print(f"it's tuple: {tpl}")
# 	case _:
# 		print("not correctly")
# # можно записать в один:
# # case (a, b, c) | (_, a, b, c, *_): print(f"it's: {a, b, c}")
# # но должны совпадать имена и количество переменных


# cmd = {"id": 822, "url": "http://pythoniscool.ru", "method": "get", "timeout": 1000}
# cmd2 = {"id": 822, "url": "http://pythoniscool.ru", "info": [121, {"method": "get", "timeout": 1000}, True, 67]}
# cmd3 = {1, 2, 3, 4, 5}

# match cmd:
# 	case {"url": str() as url, "method": "get", **kwargs} if len(kwargs) <= 2: # пример работы с dict
# 		print(url)
# 		# если есть {}, то шаблон ожидает данные именно в формате dict
# 		# проверяет по ключу "url" значение на строковый тип и берёт его
# 		# стработает только если значение по ключу "method" равно "get"
# 		# можно указать дополнительные значения по ключу "method" через оператор "|"
# 		# в if записано: не более двух доп. ключей
# 		# можно написать if not kwargs для пустого остатка
# 	case _:
# 		print("something is wrong")

# match cmd2:
# 	case {"url": str() as url, "info": [_, {"method": "get"}, _, _]}:
# 		print(url)
# 		# в списке обязательно нужное количество элементов
# 	case _:
# 		print("something is wrong")

# match cmd3:
# 	case set() as keys:
# 		print(keys)
# 	case _:
# 		print("something is wrong")
'''

#----------------------------------Разное в пайтон----------------------------------

'''
# Тернарный условный оператор
a = 2
b = 7
res = a if a > b else b # вывод: b

# Если цикл прерван с помощью break, то else не выполняется (нештатное выполнение цикла)

# // - округляет к наименьшему целому (3.5 = 3, -3.5 = -4)

# Итератор - объект, который можно перебрать

# Эллипсис (... или Ellipsis) в Python - это специальный синтаксис, 
# используемый для обозначения неполного кода. 
# Он позволяет указывать, что в определенном месте кода должно быть что-то
# дополнительное, но это не является необходимостью для выполнения программы

by = b"python" # строка в байтовом представлении (все символы байтовые, то есть равны своему байтовому аналогу)
# bites - отдельный тип данных

# Есть такая штука, как assert. Это нужно для проверки своего кода
# Можно написать либо в if __name__ == '__mait__': ..., либо в отдельных функциях
# Вписываем условие проверки и если не прошло, то выдаёт ошибку AssertionError
# Например: assert f("python") == "True"
# Практически тоже самое, что и if, но выдаст ошибку при непрохождении условия
# Можно вторым аргументом указать сообщение при провале теста: assert 1 == 2, "один не равен двум"
# Рекомендуется писать такие сообщения
'''