# 559
# Дано натуральне n. Знайти всі, менші n числа Мерсенна.
import math


def task_559():
    print('Введіть натуральне N, щоб отримати числа Мерсенна, менші n.')
    while True:
        n = input('Введіть натуральне N:\n')
        if not n.isdigit():
            print('Схоже Ви ввели не число...')
            continue
        elif n == 0:
            print('0 не є натуральним числом!')
            continue
        elif int(n) < 2:
            print('Для простих чисел Мерсена, N має бути більше 2!')
            continue
        else:
            n = int(n)
            break

    num_mers = [(2 ** i - 1) for i in range(1, n + 1)]
    simple_num = []

    # for i in range(1, n+1):
    #     num_mers.append(2 ** i - 1)
    print(
        f'Послідовність Мерсенна для натурального {n} має вигляд:\n{num_mers}')

    for count in range(2, n+1):
        i = 2
        limit = int(math.sqrt(count))
        while i <= limit:
            if count % i == 0:
                break
            i += 1
        else:
            simple_num.append(count)
    simple_num_mers = [(2 ** i + 1) for i in simple_num]
    # for i in simple_num:
    #     simple_num_mers.append(2 ** i - 1)
    print(
        f'Послідовність простих чисел Мерсенна для натурального {n} має вигляд: {simple_num_mers}')
