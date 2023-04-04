def writing_person():
    lastname = input("фамилия: ")
    name = input("имя: ")
    surname = input("отчество: ")
    tel = input("телефон: ")
    data = open("D:\обучение\python\sem8\phonebook.txt", "a", encoding="utf-8")
    data.writelines(
        f"фамилия:{lastname} имя:{name} отчество:{surname} телефон:{tel}\n")
    data.close()


def search():
    lookfor = input("кого ищем? ")
    with open("D:\обучение\python\sem8\phonebook.txt", "r", encoding="utf-8") as data:
        i = 0
        for line in data:
            if lookfor in line:
                print(str(i) + " " + line)
                i += 1
            else:
                i += 1


def print_phonebook():
    with open("D:\обучение\python\sem8\phonebook.txt", "r", encoding="utf-8") as data:
        i = 0
        for line in data:
            print(str(i) + " " + line)
            i += 1


def delete():
    delet = int(input("какую строку удалить? "))
    with open("D:\обучение\python\sem8\phonebook.txt", "r", encoding="utf-8") as data:
        array = data.readlines()
        array.pop(delet)
    with open("D:\обучение\python\sem8\phonebook.txt", "w", encoding="utf-8") as data:
        for i in array:
            data.write(str(i))


def change():
    chang = int(input("какую строку изменить? "))
    lastname = input("новая фамилия: ")
    name = input("новое имя: ")
    surname = input("новое отчество: ")
    tel = input("новый телефон: ")
    with open("D:\обучение\python\sem8\phonebook.txt", "r", encoding="utf-8") as data:
        array = data.readlines()
    array.pop(chang)
    array.insert(
        chang, f"фамилия:{lastname} имя:{name} отчество:{surname} телефон:{tel}\n")
    with open("D:\обучение\python\sem8\phonebook.txt", "w", encoding="utf-8") as data:
        for i in array:
            data.write(str(i))


def new_load():
    new_phonebook = input("введите ссылку: ")
    with open("D:\обучение\python\sem8\phonebook.txt", "r", encoding="utf-8") as data:
        input_array = data.readlines()
    with open(new_phonebook, "r", encoding="utf-8") as data:
        output_array = data.readlines()
    for elem in output_array:
        if elem not in input_array:
            input_array.append(elem)
    with open("D:\обучение\python\sem8\phonebook.txt", "w", encoding="utf-8") as data:
        for i in input_array:
            data.write(str(i))


print("""1 - добавление, 
2 - поиск, 
3 - вывод на экран, 
4 - импорт в файл,
5 - удаление,
6 - изменение """)
ask = int(input())
if ask == 1:
    writing_person()
elif ask == 2:
    search()
elif ask == 3:
    print_phonebook()
elif ask == 4:
    new_load()
elif ask == 5:
    delete()
elif ask == 6:
    change()
else:
    print("нет такой команды")