#----------------------------------Представление и мини пример

'''
# Наследование (получение способностей от родительского класса)
# Полиморфизм (переопределение методов)
# Инкапсуляция (защита)

class A:
	"Некий класс А" # описание класса
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
	def summa(self):
		return self.num1 + self.num2

class B(A): # наследование
	def __init__(self, num1, num2, num3):
		super(B, self).__init__(num1, num2)
		self.num3 = num3
	def summa(self): # полиморфизм # выбирается этот метод
		return self.num1 + self.num2 + self.num3

class C:
	pass

class D(C, B):
	pass

a = A(7, 8) # объект/экземпляр класса
b = B(1, 2, 3)
print(a.summa(), b.summa())
'''

#----------------------------------Общая теория

# Классы называем только с заглавной буквы
# Переменные внутри класса - атрибуты, а функции - методы (тоже можно считать атрибутами)
# Атрибуты класса общие для всех его объектов
# Имя класса = названию типа данных
# Класс и его атрибуты имеют свои пространства имён
# Все классы неявно наследуются от класса object

# self - ссылка на новый созданный экземпляр класса. (ссылка на текущий экземпляр класса)
# Позволяет понять программе с каким экземпляром классам мы работаем

# Можно использовать .__dict__, чтобы увидеть все атрибуты указанного класса
# Можно использовать .__doc__, чтобы увидеть описание указанного класса
# Можно использовать del, но только если атрибут присутствует в данном пространстве имён


#----------------------------------Функции для классов

# setattr(<имя класса>, <название атрибута>, <значение атрибута>)
# Она добавит новый атрибут или изменит уже созданный

# getattr(<имя класса или его объекта>, <название атрибута>, <то, что возвращать, если указанного атрибута несуществует>)
# Вернёт значения указанного атрибута, или то, что записали третьим аргументом
# Третий аргумент необязателен

# hasattr(<имя класса или его объекта>, <название атрибута>)
# Вернёт True, если такой атрибут существует в классе

# delattr(<имя класса>, <название атрибута>)
# Удалит указанный атрибут, если он существует


# class A:
# 	"Some class that love to do something"
# 	sa = 120
# 	sa2 = "python"

# setattr(A, "sa3", "some")
# delattr(A, "sa2")

# print(getattr(A, "sa"))
# print(hasattr(A, "sa2"))

# print(A.__dict__)
# print(A.__doc__)


#----------------------------------Магические методы

# Магические методы еще называют dunder-методами (от сокращения double underscope - двойное подчёркивание)

# __init__(self) - вызывается сразу после создания экземпляра класса

# __del__(self) - вызывается сразу после удаления экземпляра класса (финализатор)
# Удаление - когда сборщик мусора съедает наш объект класса

# __new__(cls, *args, **kwargs) - вызывается сразу перед созданием экземпляра класса
# cls - ссылка на текущий экземпляр класса (на сам класс)
# Нужно возвращать адрес нового созданного объекта: return super().__new__(cls) - ссылка на базовый класс (object)
# Без этой строчки экземпляр класса не будет создан

# __getattribute__(self, item) - вызывается, когда идёт обращение к атрибуту через экземпляр класса
# важно, чтобы была строчка: return object.__getattribute__(self, item)

# __setattr__(self, key, value) - вызывается, когда атрибуту присваивается новое значение
# если хотим добавить новое значение в класс в этом методе, то пишем self.__dict__[key] = value

# __getattr__(self, item) - вызывается, когда идёт обращение к несуществующему атрибуту через экземпляр класса
# можно применить так: чтобы не было ошибки можно написать return False внутри метода

# __delattr__(self, item) - вызывается, когда удаляется атрибут из экземпляра класса

# __call__(self, *args, **kwargs) - вызывается при вызове объекта класса через ()
# Простое оформление:
# obj = self.__new__(self, *args, **kwargs)
# self.__init__(obj, *args, **kwargs)
# return obj
# Классы с этим методом - функторы (можно вызывать их объекты)
# Можем дополнительно указывать какие-либо аргументы и использовать их
# Метод может использоваться для замены замыканий функций или декораторов функций

# __str__(self) - срабатывает в момент отображения информации об объекте класса (print, str) для пользователя

# __repr__(self) - срабатывает в момент отображения информации об объекте класса (при отладке) для разработчика
# Работает в режиме отладки

# __len__(self) - позволяет применять len() к объектам класса
# Другими словами: срабатывает когда используем len() к объекту класса

# __abs__(self) - позволяет применять abs() к объектам класса
# Другими словами: срабатывает когда используем abs() к объекту класса


# class A:
# 	def __new__(cls, *args, **kwargs):
# 		print("__new__:", args, kwargs)
# 		return super().__new__(cls)

# 	def __init__(self, a, b):
# 		print("__init__:", (a, b))
# 		self.a = a
# 		self.b = b
	
# 	def __del__(self):
# 		print("__del__")

# 	def __getattribute__(self, item):
# 		print("__getattribute__:", item)
# 		return object.__getattribute__(self, item)
	
# 	def __setattr__(self, key, value):
# 		print("__setattr__:", f"{key} = {value}")
# 		object.__setattr__(self, key, value)

# 	def __getattr__(self, item):
# 		print("__getattr__:", item)
	
# 	def __delattr__(self, item):
# 		print("__delattr__:", item)
# 		object.__delattr__(self, item) # чтобы атрибут удалился

# 	def __call__(self, *args, **kwargs):
# 		print("__call__")
	
# 	def __repr__(self):
# 		print("__repr__")
# 		return f"{self.__class__}: {self.a}, {self.b}"

# 	def __str__(self):
# 		print("__str__")
# 		return f"{self.a}, {self.b}"

# 	def __len__(self):
# 		print("__len__")
# 		return len(self.__dict__)

# 	def __abs__(self):
# 		print("__abs__")
# 		return abs(self.a), abs(self.b)


# pt1 = A(3, 5) # __new__ __init__ __setattr__ __setattr__
# два вызова __setattr__, так как в инит два раза присвоили новые значения

# pt1.b # __getattribute__
# pt1.new # __getattribute__ __getattr__

# pt1() # __call__

# print(pt1) # __str__ __getattribute__ __getattribute__

# print(len(pt1)) # __len__ __getattribute__
# print(abs(pt1)) # __abs__ __getattribute__ __getattribute__

# del pt1.b # __delattr__


#----------------------------------Примеры для магических методов

# __call__

# class StripChars:
# 	"Удаляет символы в начале и конце строки"
# 	def __init__(self, chars):
# 		self.__chars = chars
	
# 	def __call__(self, *args, **kwargs):
# 		if not isinstance(args[0], str):
# 			raise TypeError("Аргумент должен быть строкой")
		
# 		return args[0].strip(self.__chars)


# s = StripChars("!,.? ;:")
# res = s("  Python!! .")
# print(res)


# from math import sin, pi

# class Derivate:
# 	"Класс-декоратор, вычисляющий производные определённой функции в некой точке x"
# 	def __init__(self, func):
# 		self.__fn = func
	
# 	def __call__(self, x, dx=0.0001, *args, **kwargs):
# 		return (self.__fn(x + dx) - self.__fn(x)) / dx


# @Derivate # По другому: df_sin = Derivate(df_sin) # df_sin ссылается на объект класса Derivate
# def df_sin(x):
# 	return sin(x)


# print(df_sin(pi/3))


#----------------------------------Декораторы classmethod и staticmethod

# @classmethod
# Если создать метод с этим декоратором, то он будет работать только с атрибутами этого класса
# Обязательный параметр cls
# Можно вызывать только через сам класс
# Можно использовать внутри класса (при вызове стоит писать self.)

# @staticmethod
# Можем определить метод, кторый не имеет доступа ни к атрибутам класса (можно, но ненужно), ни к атрибутам его объектов
# Другими словами создаём функцию внутри класса, несвязанную с самим классом
# Можно вызвать вне класса (<название класса>.<название метода>) и внутри него.


# class A:
# 	minc = 0
# 	maxc = 100

# 	def __init__(self, x):
# 		self.x = 0
# 		if self.func1(x):
# 			self.x = x
		
# 			print(self.func2(x, 10))	
# 			print()
	
# 	@classmethod
# 	def func1(cls, arg):
# 		return cls.minc <= arg <= cls.maxc
	
# 	@staticmethod
# 	def func2(x, y):
# 		return x*x + y*y


# print(A.func1(5))
# print()

# a = A(60)
# print(a.__dict__)
# print()

# b = A(160)
# print(b.__dict__)
# print()

# print(A.func2(3, 4))
# print()


#----------------------------------Инкапсуляция

# Можно управлять доступом к переменным класса

# Виды режимов доступа:
# public (без подчёркиваний) - можно обращаться отовсюду
# protected (одно подчёркивание _ ) - можно обратиться внутри самого класса и в его дочерних классах
# private (два подчёркивания __ ) - можно обратиться только внутри класса

# Сама инкапсуляция не ограничивает доступ, а просто предупреждает программиста
# Но если два подчёркивания, то уже нельзя обратиться извне как обычно, но можно через кодовое имя
# Однако никогда не обращаемся к сделанным недоступными методам и атрибутам

# Если хочется еще лучше защитить методы класса, то нужен специальный модуль
# Нужно установить модуль accessify
# Будут доступны два декоратора: @private и @protected
# Просто прописываем этот декоратор к нужным методам и они будут недоступны извне
# Это крайний случай


# class A:
# 	def __init__(self, x, y):
# 		self.__x = self.__y = 0
# 		if self.__func1(x) and self.__func1(y):
# 			self.__x = x
# 			self.__y = y
	
# 	@classmethod
# 	def __func1(cls, x):
# 		return type(x) in (int, float)

# 	def set_coord(self, x, y): # сеттор
# 		if self.__func1(x) and self.__func1(y):
# 			self.__x = x
# 			self.__y = y
# 		else:
# 			raise ValueError("Только числа!")

# 	def get_coord(self): # геттор
# 		return self.__x, self.__y


# a = A(12, 69)

# a.set_coord(0, 0)

# print(a.get_coord())

# # print(a._x, a.__y) - ошибка


#----------------------------------Паттерн "Моносостояние"

# Идея моносостояния: есть многопоточный процесс, и в каждом потоке создаётся экземпляр класса
# Хочется, чтобы все экземпляры имели единые локальные свойства, то есть общие для всех экземпляров класса
# При изменении любого экземпляра, все другие тоже меняются

# Реализация:
# class ThreadData:
# 	__shared_attrs = {
# 		"name": "thread_1",
# 		"data": {},
# 		"id": 1,
# 	}

# 	def __init__(self):
# 		self.__dict__ = self.__shared_attrs


# th1 = ThreadData()
# th2 = ThreadData()
# th3 = ThreadData()
# th4 = ThreadData()

# th2.id = 3
# th4.new_attr = "new_attr"

# print(th1.__dict__)
# print(th2.__dict__)
# print(th3.__dict__)
# print(th4.__dict__)

# __dict__ каждого экземпляра будет ссылаться на один и тот же словарь
# В каждом экземпляре его словарь __dict__ ссылается на один и тот же наш словарь __shared_attrs
# Можно так же создавать новые свойства


#----------------------------------Декоратор property

# Преоритет выполнения выше, чем преоритет у любого локального свойства
# Используют для удобства 
# Через один атрибут происходит взаимодействие, а не через напрямую через сеттор и геттор
# 

# class Person:
# 	def __init__(self, name, old):
# 		self.__name = name
# 		self.__old = old
	
# 	def get_old(self):
# 		return self.__old

# 	def set_old(self, old):
# 		self.__old = old

# 	old = property(get_old, set_old)


# p = Person("Антонио Фагундас", 35)

# print(p.old)

# p.old = 20
# print(p.__dict__)

# Строчку old = property(get_old, set_old) можно записать иначе через декораторы

# Так:
# old = property()
# old = old.setter(set_old)
# old = old.getter(get_old)

# Или так
# Перед геттором: @property
# Перед сеттором: @<имя метода к которому прописали @property>.setter
# Имена сеттора и геттора должны совпадать в таком случае
# Такой способ используют чаще

# Еще у этого декоратора есть свойство deleter (вызывается при удалении свойства)
# def old(self):
# 	del self.__old
# Свойство можно потом создать снова


# # Пример использования
# from string import ascii_letters

# class Person:
# 	S_RUS = "йцукенгшщзхъфывапролджэячсмитьбюё-"
# 	S_RUS_UPPER = S_RUS.upper()

# 	def __init__(self, fio, old, ps, weight):
# 		self.verify_fio(fio)

# 		self.__fio = fio.split() # ФИО (список из)
# 		self.old = old # возраст (целое число от 14 до 120)
# 		self.ps = ps # серия и номер паспорта (формат: хххх хххххх, где х - цифра)
# 		self.weight = weight # вес в кг (вещественное число от 20)
	
# 	@classmethod
# 	def verify_fio(cls, fio):
# 		if type(fio) != str:
# 			raise TypeError("ФИО должно быть строкой")

# 		f = fio.split()
# 		if len(f) != 3:
# 			raise TypeError("Неверный формат ФИО")
		
# 		letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
# 		for s in f:
# 			if len(s) < 1:
# 				raise TypeError("В ФИО должен быть хотя бы один символ")
# 			if len(s.strip(letters)) != 0:
# 				raise TypeError("Только буквенные символы и дефис в ФИО")

# 	@classmethod
# 	def verify_old(cls, old):
# 		if type(old) != int or old < 14 or old > 120:
# 			raise TypeError("Возрасть должен быть целым числом в диапазоне [14; 120]")

# 	@classmethod
# 	def verify_weight(cls, weight):
# 		if type(weight) != float or weight < 20:
# 			raise TypeError("Вес должен быть вещественным числом от 20")

# 	@classmethod
# 	def verify_ps(cls, ps):
# 		if type(ps) != str:
# 			raise TypeError("Паспорт должно быть строкой")
	
# 		s = ps.split()
# 		if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
# 			raise TypeError("Неверный формат паспорта")

# 		for p in s:
# 			if not p.isdigit():
# 				raise TypeError("Серия и номер должны быть числами")
		
# 	@property
# 	def fio(self):
# 		return self.__fio
	
# 	@property
# 	def old(self):
# 		return self.__old

# 	@old.setter
# 	def old(self, old):
# 		self.verify_old(old)
# 		self.__old = old
	
# 	@property
# 	def weight(self):
# 		return self.__weight

# 	@weight.setter
# 	def weight(self, weight):
# 		self.verify_weight(weight)
# 		self.__weight = weight
	
# 	@property
# 	def ps(self):
# 		return self.__ps
	
# 	@ps.setter
# 	def ps(self, ps):
# 		self.verify_ps(ps)
# 		self.__ps = ps

# p = Person("Режин Эдуарти Фаликард", 30, "1234 567890", 80.0)
# p.old = 100
# p.ps = "1111 121212"
# p.weight = 90.0
# print(p.__dict__)

# Тут сетторы срабатывают и в инит, проверяя данные


#----------------------------------Дескрипторы (data descriptor и non-data descriptor)

# non-data descriptor: если класс содержит магический метод __get__(self, instance, owner)
# Может только считывать данные и имеет тот же преоритеть доступа, что и обычные атрибуты
# data descriptor: если класс содержит дополнительно магический метод: 
# __set__(self, instance, value) или __del__(self) или оба
# Дескрипторы редко используют
# Дескриптор - отдельный класс для улучшения читаемости кода (чтобы не писать одно и тоже)

# Пример
# class ReadIntX: # non-data descriptor
# 	def __set_name__(self, owner, name):
# 		self.name = "_x"

# 	def __get__(self, instance, owner):
# 		return getattr(instance, self.name)

# class Intenger: # data descriptor
# 	@classmethod
# 	def verify_coord(cls, coord): # проверка на тип int
# 		if type(coord) != int:
# 			raise TypeError("Координата должна быть целым числом")

# 	def __set_name__(self, owner, name): # метод вызывается при создании объекта
# 		self.name = "_" + name
# 	# self - сслыка на пространство имён x
# 	# owner - сслыка на класс Point3D
# 	# name - название объекта класса Intenger
	
# 	def __get__(self, instance, owner):
# 		return instance.__dict__[self.name] # можно написать иначе: getattr(instance, self.name)
# 	# self - сслыка на пространство имён x
# 	# instance - ссылка на объект класса Point3D
# 	# owner - сслыка на класс Point3D

# 	def __set__(self, instance, value):
# 		self. verify_coord(value)
# 		instance.__dict__[self.name] = value # можно написать иначе: setattr(instance, self.name, value)
# 	# self - сслыка на пространство имён x
# 	# instance - ссылка на объект класса Point3D
# 	# value - то, что присваиваем


# class Point3D:
# 	x = Intenger()
# 	y = Intenger()
# 	z = Intenger()
# 	xr = ReadIntX()

# 	def __init__(self, x, y, z):
# 		self.x = x
# 		self.y = y
# 		self.z = z


# pt = Point3D(1, 2, 3)
# pt.xr = 5 # просто создали локальный атрибут, словно нет дескриптора. Преоритет такой же
# # Преоритет у data descriptor больше, чем у локальных атрибутов
# print(pt.__dict__, pt.xr)