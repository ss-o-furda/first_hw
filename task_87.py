# 87
# Дано натуральні n, m. Отримати суму m останніх цифр числа n.


def task_87(seq):
    n, m = seq[0], seq[1]
    result = sum(n[-m:])

    return result

