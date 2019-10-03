import task_87
import task_226
import task_559


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
            m, N, result = task_87.task_87()
            print(f'Сума {m} останніх цифр числа {N} = {result}')
            break
        elif int(number) == 226:
            print('*' * 100)
            n, m, mn, s_k_n, s_k_m, s_k = task_226.task_226()
            print(f'Числа, кратні {n} у проміжку 1..{mn}:\n{s_k_n}')
            print(f'Числа, кратні {m} у проміжку 1..{mn}:\n{s_k_m}')
            print(f'Числа, кратні {n} та {m} у проміжку 1..{mn}: {s_k}')
            break
        elif int(number) == 559:
            print('*' * 100)
            n, num_mers, simple_num_mers = task_559.task_559()
            print(
                f'Послідовність Мерсенна для натурального {n} має вигляд:\n{num_mers}')
            print(
                f'Послідовність простих чисел Мерсенна для натурального {n} має вигляд: {simple_num_mers}')
            break
        else:
            print(f'Завдання з номером {number} не існує')
            continue
        break


if __name__ == "__main__":
    main()
