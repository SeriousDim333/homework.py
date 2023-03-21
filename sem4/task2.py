# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

n = int(input("количество кустов = "))
trees = [randint(0, 10) for _ in range(n)]
print("грядка:")
print(trees)

max_strawberry = 0
num_of_tree = None
for i in range(-1, len(trees)-1):
    if trees[i-1] + trees[i] + trees[i+1] > max_strawberry:
        max_strawberry = trees[i-1] + trees[i] + trees[i+1]
        num_of_tree = i
if num_of_tree == -1:
    num_of_tree = len(trees)-1
print(f"{max_strawberry} ягод можно собрать напротив {num_of_tree+1} куста")
