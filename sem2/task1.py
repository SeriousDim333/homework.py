# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

coins = int(input("введите количество монет: "))
head = 0
tail = 0
for i in range(coins):
    i = randint(0,1)
    print(i)
    if i == 0:
        tail+=1
    else:
        head+=1
print(f"min coins = {head if head<tail else tail}")