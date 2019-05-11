import random

# 突然変異


def mutation(pop, pm):
    px = len(pop)
    py = len(pop[0])
    
    for i in range(px):
        if random.random() < pm:
            mpoint = random.randint(0, py-1)
            if pop[i][mpoint] == 1:
                pop[i][mpoint] = 0
            else:
                pop[i][mpoint] = 1


if __name__ == '__main__':
    pass
