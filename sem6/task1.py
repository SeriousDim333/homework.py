# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def fill_array(first_digit, dif, size):
    result = [first_digit+(i-1)*dif for i in range(1, size+1)]
    return result


a, b, c = int(input("первое число = ")), int(
    input("шаг = ")), int(input("длина = "))
print(fill_array(a, b, c))
