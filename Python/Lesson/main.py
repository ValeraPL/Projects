import os
import functions as func

"""Инициализация массивов"""
arrayName = []
tupleName = ()
dictName = {}

def main():
	"""Запрашивает комманду и вызывает функции из модуля functions"""
	querry = input(">>>: ")

	if querry == "index":
		os.system("clear")
		func.index(arrayName)
		main()
	elif querry == "count":
		os.system("clear")
		func.count(arrayName)
		main()
	elif querry == "pop":
		os.system("clear")
		func.pop(arrayName)
		main()
	elif querry == "clear":
		os.system("clear")
		func.clear(arrayName)
		main()
	elif querry == "list":
		os.system("clear")
		func.list(arrayName)
		main()
	elif querry == "tuple":
		os.system("clear")
		func.tup(arrayName)
		main()
	elif querry == "info":
		os.system("clear")
		func.info()
		main()
	elif querry == "create":
		os.system("clear")
		createArray()
	elif querry == "write":
		os.system("clear")
		func.writeFile(arrayName)
		main()
	elif querry == "read":
		os.system("clear")
		func.readFile()
		main()
	elif querry == "exit":
		os.system("clear")
		exit(0)
	else:
		print("Такой функции нет")
		main()

def createArray():
	"""Запрашивает размер массива, элементы"""
	try:
		sizeArray = int(input("Введите размер массива >>>: "))
	except ValueError:
		print("Вы должны ввести число")
		createArray()

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