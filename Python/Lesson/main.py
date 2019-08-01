arrayName = []
tupleName = ()

def index():
	request = input("Введите имя >>>: ")
	print("Имя:", request, ",", "Индекс:", arrayName.index(request))

def count():
	request = input("Введите имя >>>: ")
	print("Имя:", request, ",", "Количество:", arrayName.count(request))

def pop():
	request = int(input("Введите индекс элемента >>>: "))
	print("Имя:", arrayName[request], "Удалить[Y/N]")
	choice = input(">>>: ")
	
	if choice == "y":
		arrayName.pop(request)
		print("Удалено")
	elif choice == "n":
		main()

def clear():
	arrayName.clear()
	print("Весь массив отчищен")

def list():
	for i in arrayName:
		print(i)

def tup():
	tupleName = arrayName
	print("Массив помещен в кортеж")

def writeFile():
	nameFile = input("Введите название файла >>>: ")
	file = open(nameFile, "w")

	for i in arrayName:
		file.write("Имя: " + i + "\n")

	print("Записано")

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