# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

n, m = int(input("кол-во элементов первого множества = ")), int(input("кол-во элементов второго множества = "))
first_set = {randint(0, 10) for _ in range(n)}
print("первое множество:")
print(first_set)
second_set = {randint(0, 10) for _ in range(m)}
print("второе множество")
print(second_set)

uniq_set = first_set.intersection(second_set)
if  uniq_set:
    print("числа которые повторяются")
    print(uniq_set)

    result = []
    for i in range(len(uniq_set)):
        result.append(min(uniq_set))
        uniq_set.discard(min(uniq_set))
    print("по возрастанию")
    print(*result)
else:
    print("нет совпадений, попробуйте еще раз")
