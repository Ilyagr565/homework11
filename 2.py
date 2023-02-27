s = int(input('Введите сумму числе: '))
p = int(input('Введите произведение: '))
a = 0
for x in range(s):
    for y in range(s):
        if x + y == s and x * y == p:
            a += 1
            print(x, y)
if a == 0:
    print('Вы ввели не корректные данные!')