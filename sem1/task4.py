# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой
# между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

width = int(input("введите количество долек в ширину: "))
long = int(input("введите количество долек в длину: "))
slice = int(input("сколько долек вы хотите отломить: "))

if slice % width == 0 or slice % long == 0:
    print("yes")
else:
    print("no")
