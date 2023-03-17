# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

element_amount = int(input("введите количество элементов в массиве: "))
numbers = [randint(0, 100) for _ in range(element_amount)]
print(numbers)

num_search = int(input("какое число ищем? "))
min = 1000
temp = 0
for i in numbers:
    if abs(i - num_search) < min:
        min = abs(i - num_search)
        temp = i
print(f"самое близкое {temp}")
