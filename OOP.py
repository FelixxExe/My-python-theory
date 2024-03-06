#----------------------------------ООП----------------------------------

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


# pt1 = A(3, 5) # __new__ __init__ __setattr__ __setattr__
# # два вызоова __setattr__, так как в инит два раза присвоили новые значения

# pt1.b # __getattribute__
# pt1.new # __getattribute__ __getattr__

# del pt1.b # __delattr__


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
# data descriptor: если класс содержит дополнительно магический метод: 
# __set__(self, instance, value) или __del__(self) или оба
# 
# 
