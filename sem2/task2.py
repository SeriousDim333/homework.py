# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input("введите сумму чисел: "))
p = int(input("введите произведение чисел: "))

d = s*s - 4*p
if d<0:
    print("таких чисел нет")
else:
    x = int(((s- d**(1/2))/2))
    y = s -x
    print(f"загаданные числа: {x,y}")