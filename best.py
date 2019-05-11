# 最適解と最適解の遺伝子を探す


def best(pop, fit_value):
    px = len(pop)
    max_indi1 = []
    max_indi2 = []
    max_indi3 = []

    min_indi1 = []
    min_indi2 = []
    min_indi3 = []

    max_fit = min_fit = fit_value[0]
    for i in range(1, px):
        if fit_value[i] > max_fit:
            max_fit = fit_value[i]
            max_indi1 = pop[i % px]
            max_indi2 = pop[(i + 1) % px]
            max_indi3 = pop[(i + 2) % px]
        if fit_value[i] < min_fit:
            min_fit = fit_value[i]
            min_indi1 = pop[i % px]
            min_indi2 = pop[(i + 1) % px]
            min_indi3 = pop[(i + 2) % px]
    return [max_indi1, max_indi2, max_indi3, max_fit, min_indi1, min_indi2, min_indi3, min_fit]


if __name__ == '__main__':
    pass
