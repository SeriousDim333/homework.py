# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4


def summa(a, b):
    if b == 1:
        return a+1
    return summa(a, b-1)+1


a, b = int(input("первое число: ")), int(
    input("второе число: "))
print(summa(a, b))
