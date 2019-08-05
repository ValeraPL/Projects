arrayName = []
tupleName = ()

def index():
	request = input("index: Введите имя >>>: ")
	
	try:
		print("Имя:", request, ",", "Индекс:", arrayName.index(request))
		main()
	except ValueError as e:
		print("Имя:", request, "не найдено")
		index()

def count():
	request = input("count: Введите имя >>>: ")

	if arrayName.count(request) == 0:
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
			print("Удалено")
		elif choice == "n":
			main()
	except IndexError as e:
		print("Индекс:", request, "не найдено")
		pop()

def clear():
	choice = input("clear: Отчистить массив[Y/N]? >>>: ")

	if choice == "y":
		arrayName.clear()
		print("Весь массив отчищен")
	elif choice == "n":
		main()

def list():
	for i in arrayName:
		print(i)

def tup():
	tupleName = arrayName
	print("Массив помещен в кортеж")

def writeFile():
	writeFileName = input("write: Введите название файла >>>: ")
	wFile = open(writeFileName, "w")

	for i in arrayName:
		wFile.write("Имя: " + i + "\n")

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
		index()
		main()
	elif querry == "count":
		count()
		main()
	elif querry == "pop":
		pop()
		main()
	elif querry == "clear":
		clear()
		main()
	elif querry == "list":
		list()
		main()
	elif querry == "tuple":
		tup()
		main()
	elif querry == "info":
		info()
		main()
	elif querry == "create":
		createArray()
	elif querry == "write":
		writeFile()
		main()
	elif querry == "read":
		readFile()
		main()
	elif querry == "exit":
		exit(0)
	else:
		print("Такой функции нет")
		main()

def createArray():
	sizeArray = int(input("Введите размер массива >>>: "))

	for i in range(sizeArray):
		arrayName.append(input("Введите имя >>>: "))

	for j in arrayName:
		print(j)

	choice = input("Все верно[Y/N]? >>>: ")
	if choice == "n":
		arrayName.clear()
		createArray()
	elif choice == "y":
		main()

createArray()