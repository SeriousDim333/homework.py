# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


def check_ritm(s):
    vowels = ["а", "и", "е", "ё", "о", "у", "ы", "э", "ю", "я"]
    array = s.split()
    array_vowels = list()
    for i in array:
        array_vowels.append(list(filter(lambda x: x in vowels, i)))
    arrays_lens = set(map(lambda x: len(x), array_vowels))
    if len(arrays_lens) < 2:
        print("Парам пам-пам")
    else:
        print("Пам парам")


s = "пара-ра-рам рам-пам-папам па-ра-па-да"
check_ritm(s)
