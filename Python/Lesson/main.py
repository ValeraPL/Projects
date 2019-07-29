arrayName = []
sizeArray = int(input("Введите размер массива >>>: "))
i = 0
info = """index: Узнать индекс элемента\ncount: Узнать количество схожих элементов\npop: Удалить элемент по индексу"""

while i < sizeArray:
	setName = input("Введите имя >>>: ")
	arrayName.append(setName)
	i += 1

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