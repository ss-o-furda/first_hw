# 226
# Дано натуральні n, m. Отримати всі їх натуральні спільні кратні, менші mn


def task_226(seq):
    n, m = seq[0], seq[1]
    mn = m * n
    s_k_n = [i for i in range(1, mn + 1) if i % n == 0]
    s_k_m = [i for i in range(1, mn + 1) if i % m == 0]
    # for i in range(1, mn+1):
    #     if i % n == 0:
    #         s_k_n.append(i)
    #     if i % m == 0:
    #         s_k_m.append(i)
    s_k = sorted(list(set(s_k_n) & set(s_k_m)))

    return s_k_n, s_k_m, s_k
