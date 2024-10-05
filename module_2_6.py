def one(num):
    win = ''
    for i in range(1, num):
        for j in range(2, num):
            if j <= i:
                continue
            elif num % (i + j) == 0:
                win += str(i) + str(j)
    return win

n = int(input('Введите любое целое число от 3 до 20 включительно: '))
result = one(n)
print('Ваш пароль:', result)