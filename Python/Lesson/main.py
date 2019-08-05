import os

arrayName = []
tupleName = ()
dictName = {}

def index():
	request = input("index: Введите имя >>>: ")
	
	try:
		print("Имя:", request, ",", "Индекс:", arrayName.index(request))
		main()
	except ValueError as e:
		os.system("clear")
		print("Имя:", request, "не найдено")
		index()

def count():
	request = input("count: Введите имя >>>: ")

	if arrayName.count(request) == 0:
		os.system("clear")
		print("Имя:", request, "не найдено")
		count()
	else:
		print("Имя:", request, ",", "Количество:", arrayName.count(request))
		main()

def pop():
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
	choice = input("clear: Отчистить массив[Y/N]? >>>: ")

	if choice == "y":
		os.system("clear")
		arrayName.clear()
		print("Весь массив отчищен")
	elif choice == "n":
		os.system("clear")
		main()

def list():
	os.system("clear")
	for i in arrayName:
		print(i)

def tup():
	os.system("clear")
	tupleName = arrayName
	print("Массив помещен в кортеж")

def writeFile():
	writeFileName = input("write: Введите название файла >>>: ")
	wFile = open(writeFileName, "w")

	for i in arrayName:
		wFile.write("Имя: " + i + "\n")

	os.system("clear")

	print("Записано")

	wFile.close()

def readFile():
	readFileName = input("read: Введите название файла >>>: ")
	rFile = open(readFileName, "r")
	handle = rFile.read()
	print(handle)

def info():
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

def main():
	querry = input(">>>: ")

	if querry == "index":
		os.system("clear")
		index()
		main()
	elif querry == "count":
		os.system("clear")
		count()
		main()
	elif querry == "pop":
		os.system("clear")
		pop()
		main()
	elif querry == "clear":
		os.system("clear")
		clear()
		main()
	elif querry == "list":
		os.system("clear")
		list()
		main()
	elif querry == "tuple":
		os.system("clear")
		tup()
		main()
	elif querry == "info":
		os.system("clear")
		info()
		main()
	elif querry == "create":
		os.system("clear")
		createArray()
	elif querry == "write":
		os.system("clear")
		writeFile()
		main()
	elif querry == "read":
		os.system("clear")
		readFile()
		main()
	elif querry == "exit":
		os.system("clear")
		exit(0)
	else:
		print("Такой функции нет")
		main()

def createArray():
	os.system("clear")

	sizeArray = int(input("Введите размер массива >>>: "))

	for i in range(sizeArray):
		arrayName.append(input("Введите имя >>>: "))

	for j in arrayName:
		print(j)

	print("Размер массива: " + str(sizeArray))

	choice = input("Все верно[Y/N]? >>>: ")
	if choice == "n":
		os.system("clear")
		arrayName.clear()
		createArray()
	elif choice == "y":
		os.system("clear")
		main()

createArray()