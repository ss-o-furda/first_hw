import task_87, task_226, task_559

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
            task_87.task_87()
            break
        elif int(number) == 226:
            print('*' * 100)
            task_226.task_226()
            break
        elif int(number) == 559:
            print('*' * 100)
            task_559.task_559()
            break
        else:
            print(f'Завдання з номером {number} не існує')
            continue
        break

if __name__ == "__main__":
    main()