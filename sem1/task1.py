# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = input("введите трёх значное число: ")
if len(number) == 3:
    result = int(number[0])+int(number[1])+int(number[2])
    print(f"сумма всех цифр числа {number} = {result}")
else:
    print("это не трёх значное число")
