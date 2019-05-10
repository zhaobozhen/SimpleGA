# 0.0 coding:utf-8 0.0
# 找出最优解和最优解的基因编码


def best(pop, fit_value):
    px = len(pop)
    best_individual1 = []
    best_individual2 = []
    best_individual3 = []
    best_fit = fit_value[0]
    for i in range(1, px):
        if fit_value[i] > best_fit:
            best_fit = fit_value[i]
            best_individual1 = pop[i % len(pop)]
            best_individual2 = pop[(i + 1) % len(pop)]
            best_individual3 = pop[(i + 2) % len(pop)]
    return [best_individual1, best_individual2, best_individual3, best_fit]


if __name__ == '__main__':
    pass
