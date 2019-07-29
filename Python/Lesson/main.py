arrayName = []
sizeArray = int(input("Введите размер массива >>>: "))
info = """list: Просмотреть весь массив\nindex: Узнать индекс элемента\ncount: Узнать количество схожих элементов\npop: Удалить элемент по индексу\nclear: Отчистить весь массив"""

for i in range(sizeArray):
	arrayName.append(input("Введите имя >>>: "))

print(info)

querry = input(">>>: ")

if querry == "index":
	request = input("Введите имя >>>: ")
	print("Имя:", request, ",", "Индекс:", arrayName.index(request))
elif querry == "count":
	request = input("Введите имя >>>: ")
	print("Имя:", request, ",", "Количество:", arrayName.count(request))
elif querry == "pop":
	request = int(input("Введите индекс элемента >>>: "))
	arrayName.pop(request)
	print("Имя:", arrayName[request], "Удалено")
elif querry == "clear":
	arrayName.clear()
	print("Весь массив отчищен")
elif querry == "list":
	for index in arrayName:
		print(index)
else:
	print("Такой функции нет")