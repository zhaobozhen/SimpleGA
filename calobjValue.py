# 0.0 coding:utf-8 0.0
# 解码并计算值

import math


def decodechrom(pop, chrom_length):
    temp = []
    for i in range(len(pop)):
        t = 0
        for j in range(chrom_length):
            t += pop[i][j] * (math.pow(2, j))
        temp.append(t)
    return temp


def calobjValue(pop, chrom_length, max_value):
    obj_value = []
    temp1 = decodechrom(pop, chrom_length)
    for i in range(len(temp1)):
        x1 = temp1[i % len(temp1)] * max_value / (math.pow(2, chrom_length) - 1)
        x2 = temp1[(i+1) % len(temp1)] * max_value / (math.pow(2, chrom_length) - 1)
        x3 = temp1[(i+2) % len(temp1)] * max_value / (math.pow(2, chrom_length) - 1)
        obj_value.append(2 * math.pow(x1, 2) - 3 * math.pow(x2, 2) - 4 * x1 + 5 * x2 + x3)
    return obj_value


if __name__ == '__main__':
    pass
