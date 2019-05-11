# 選択

import random


def sum(fit_value):
    total = 0
    for i in range(len(fit_value)):
        total += fit_value[i]
    return total


def cumsum(fit_value):
    for i in range(len(fit_value) - 2, -1, -1):
        t = 0
        j = 0
        while j <= i:
            t += fit_value[j]
            j += 1
        fit_value[i] = t
        fit_value[len(fit_value) - 1] = 1


def selection(pop, fit_value):
    newfit_value = []

    fit_value.sort()
    temp = fit_value[0]
    for i in range(0, len(fit_value)):
        fit_value[i] -= temp

    # 適応度の合計
    total_fit = sum(fit_value) + 1
    for i in range(1, len(fit_value)):
        newfit_value.append(fit_value[i] / total_fit)
    # 累積確率を計算
    cumsum(newfit_value)
    ms = []
    pop_len = len(pop)
    for i in range(pop_len):
        ms.append(random.random())
    ms.sort()
    fitin = 0
    newin = 0
    newpop = pop
    # ルーレット選択
    while newin < pop_len:
        if ms[newin] < newfit_value[fitin]:
            newpop[newin] = pop[fitin]
            newin = newin + 1
        else:
            fitin = fitin + 1


if __name__ == '__main__':
    pass
