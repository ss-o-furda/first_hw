import task_87
import task_226
import task_559


def input_for_87_task():
    print('Введіть натуральні N i M, щоб отримати суму m останніх цифр числа n.')
    while True:
        n = input('Введіть натуральне N:\n')
        if not n.isdigit():
            print('Схоже Ви ввели не число...')
            continue
        elif n == 0:
            print('0 не є натуральним числом!')
            continue
        else:
            n = list(map(int, n))
            while True:
                m = input('Введіть натуральне M:\n')
                if not m.isdigit():
                    print('Схоже Ви ввели не число...')
                    continue
                elif m == 0:
                    print('0 не є натуральним числом!')
                    continue
                elif int(m) > len(n):
                    print(
                        f'Вибачте, але у максимальне значення для M може бути {len(n)}')
                    continue
                else:
                    m = int(m)
                    break
            break
    return [n, m]

def input_for_226_task():
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
    return [n, m]

def input_for_559_task():
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
    return n


def main():
    print('*' * 100)
    print('Привітульки :)')
    print('Виберіть номер завдання, яке потрібно виконати(доступні: 87, 226, 559):')
    print('*' * 100)

    while True:
        number = input()
        if not number.isdigit():
            print('Схоже, ви ввели не число...')
            continue
        elif int(number) == 87:
            print('*' * 100)
            result = task_87.task_87(input_for_87_task())
            print(f'Сума m останніх цифр n = {result}')
            break
        elif int(number) == 226:
            print('*' * 100)
            s_k_n, s_k_m, s_k = task_226.task_226(input_for_226_task())
            print(f'Числа, кратні n:\n{s_k_n}')
            print(f'Числа, кратні m:\n{s_k_m}')
            print(f'Числа, кратні n та m: {s_k}')
            break
        elif int(number) == 559:
            print('*' * 100)
            num_mers, simple_num_mers = task_559.task_559(input_for_559_task())
            print(
                f'Послідовність Мерсенна для натурального n має вигляд:\n{num_mers}')
            print(
                f'Послідовність простих чисел Мерсенна для натурального n має вигляд: {simple_num_mers}')
            break
        else:
            print(f'Завдання з номером {number} не існує')
            continue
        break


if __name__ == "__main__":
    main()
