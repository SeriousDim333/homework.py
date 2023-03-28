# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def fill_array(size):
    array = [randint(1,10) for _ in range(size)]
    print(array)
    return array


n = int(input("размер массива = "))
array = fill_array(n)
small = int(input("нижняя граница = "))
large = int(input("верхняя граница = "))
arr_check = [i for i in range(small,large+1)]
for i in range(len(array)):
    if array[i] in arr_check:
        print(i, end = " ")
