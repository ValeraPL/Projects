import os

def index(array):
	"""Запрашивает имя и выводит индекс элемента"""
	request = input("index: Введите имя >>>: ")
	
	try:
		print("Имя:", request, ",", "Индекс:", array.index(request))
	except ValueError as e:
		os.system("clear")
		print("Имя:", request, "не найдено")
		index(array)

def count(array):
	"""Запрашивает имя выводит количество одинаковых элементов"""
	request = input("count: Введите имя >>>: ")

	if array.count(request) == 0:
		os.system("clear")
		print("Имя:", request, "не найдено")
		count(array)
	else:
		print("Имя:", request, ",", "Количество:", array.count(request))

def pop(array):
	"""Запрашивает индекс и удаляет элемент"""
	request = int(input("pop: Введите индекс элемента >>>: "))

	try:
		print("Имя:", array[request], "Удалить[Y/N]")
		choice = input("pop: >>>: ")

		if choice == "y":
			array.pop(request)
			os.system("clear")
			print("Удалено")
		elif choice == "n":
			os.system("clear")
	except IndexError:
		os.system("clear")
		print("Индекс:", request, "не найдено")
		pop(array)
	except ValueError:
		os.system("clear")
		print("Введите индекс(Число)")

def clear(array):
	"""Отчистка массива"""
	choice = input("clear: Отчистить массив[Y/N]? >>>: ")

	if choice == "y":
		os.system("clear")
		array.clear()
		print("Весь массив отчищен")
	elif choice == "n":
		os.system("clear")

def list(array):
	"""Вывод элементов"""
	os.system("clear")
	for i in array:
		print(i)

def tup(array):
	"""Помещение в кортеж"""
	os.system("clear")
	tupleName = array
	print("Массив помещен в кортеж")

def writeFile(array):
	"""Запрашивает имя файла и и записывает массив в файл"""
	writeFileName = input("write: Введите название файла >>>: ")
	wFile = open(writeFileName, "w")

	for i in array:
		wFile.write("Имя: " + i + "\n")

	os.system("clear")

	print("Записано")

	wFile.close()

def readFile():
	"""Запрашивает имя файла и выводит содержимое"""
	readFileName = input("read: Введите название файла >>>: ")
	rFile = open(readFileName, "r")
	handle = rFile.read()
	print(handle)

def info():
	"""Выводит все комманды"""
	commands = """
		tuple: Поместить массив в кортеж
		list: Просмотреть весь массив
		index: Узнать индекс элемента
		count: Узнать количество схожих элементов
		pop: Удалить элемент по индексу
		create: Создать массив
		clear: Отчистить весь массив
		write: Записать массив в файл
		read: Прочитать файл
	"""

	print(commands)