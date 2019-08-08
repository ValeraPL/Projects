def index(arrayName):
	"""Запрашивает имя и выводит индекс элемента"""
	request = input("index: Введите имя >>>: ")
	
	try:
		print("Имя:", request, ",", "Индекс:", arrayName.index(request))
	except ValueError as e:
		os.system("clear")
		print("Имя:", request, "не найдено")
		index()

def count():
	"""Запрашивает имя выводит количество одинаковых элементов"""
	request = input("count: Введите имя >>>: ")

	if arrayName.count(request) == 0:
		os.system("clear")
		print("Имя:", request, "не найдено")
		count()
	else:
		print("Имя:", request, ",", "Количество:", arrayName.count(request))
		main()

def pop():
	"""Запрашивает индекс и удаляет элемент"""
	request = int(input("pop: Введите индекс элемента >>>: "))

	try:
		print("Имя:", arrayName[request], "Удалить[Y/N]")
		choice = input("pop: >>>: ")

		if choice == "y":
			arrayName.pop(request)
			os.system("clear")
			print("Удалено")
		elif choice == "n":
			os.system("clear")
			main()
	except IndexError as e:
		os.system("clear")
		print("Индекс:", request, "не найдено")
		pop()

def clear():
	"""Отчистка массива"""
	choice = input("clear: Отчистить массив[Y/N]? >>>: ")

	if choice == "y":
		os.system("clear")
		arrayName.clear()
		print("Весь массив отчищен")
	elif choice == "n":
		os.system("clear")
		main()

def list():
	"""Вывод элементов"""
	os.system("clear")
	for i in arrayName:
		print(i)

def tup():
	"""Помещение в кортеж"""
	os.system("clear")
	tupleName = arrayName
	print("Массив помещен в кортеж")

def writeFile():
	"""Запрашивает имя файла и и записывает массив в файл"""
	writeFileName = input("write: Введите название файла >>>: ")
	wFile = open(writeFileName, "w")

	for i in arrayName:
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