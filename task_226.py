# 226
# Дано натуральні n, m. Отримати всі їх натуральні спільні кратні, менші mn


def task_226():
    print('Введіть натуральні N i M, щоб отримати всі їх натуральні спільні кратні, менші mn.')
    while True:
        n = input('Введіть натуральне N:\n')
        if not n.isdigit():
            print('Схоже Ви ввели не число...')
            continue
        elif n == 0:
            print('0 не є натуральним числом!')
            continue
        else:
            n = int(n)
            while True:
                m = input('Введіть натуральне M:\n')
                if not m.isdigit():
                    print('Схоже Ви ввели не число...')
                    continue
                elif m == 0:
                    print('0 не є натуральним числом!')
                    continue
                else:
                    m = int(m)
                    break
            break

    mn = m * n
    s_k_n = [i for i in range(1, mn + 1) if i % n == 0]
    s_k_m = [i for i in range(1, mn + 1) if i % m == 0]
    # for i in range(1, mn+1):
    #     if i % n == 0:
    #         s_k_n.append(i)
    #     if i % m == 0:
    #         s_k_m.append(i)
    print(f'Числа, кратні {n} у проміжку 1..{mn}:\n{s_k_n}')
    print(f'Числа, кратні {m} у проміжку 1..{mn}:\n{s_k_m}')
    s_k = sorted(list(set(s_k_n) & set(s_k_m)))
    print(f'Числа, кратні {n} та {m} у проміжку 1..{mn}: {s_k}')
