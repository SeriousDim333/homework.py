# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1


from random import randint

element_amount = int(input("введите количество элементов в массиве: "))
numbers = [randint(0, 10) for _ in range(element_amount)]
print(numbers)

elem_search = int(input("какое число считаем? "))
count = 0
for i in numbers:
    if i == elem_search:
        count += 1
print(f"число {elem_search} встречается {count} раз")
