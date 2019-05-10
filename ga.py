# 0.0 coding:utf-8 0.0

import matplotlib.pyplot as plt
import math

from calobjValue import calobjValue
from selection import selection
from crossover import crossover
from mutation import mutation
from best import best
from geneEncoding import geneEncoding

print('y = 2 * x1 ^ 2 - 3 * x2 ^ 2 - 4 * x1 + 5 * x2 + x3')


# 计算2进制序列代表的数值
def b2d(b, max_value, chrom_length):
	t = 0
	for j in range(len(b)):
		t += b[j] * (math.pow(2, j))
	t = t * max_value / (math.pow(2, chrom_length) - 1)
	return t


pop_size = 100		# 种群数量
max_value = 15      # 基因中允许出现的最大值
chrom_length = 4		# 染色体长度
pc = 0.6			# 交配概率
pm = 0.01           # 变异概率
results = [[]]		# 存储每一代的最优解，N个二元组
fit_value = []		# 个体适应度
fit_mean = []		# 平均适应度

# pop = [[0, 1, 0, 1] for i in range(pop_size)]
pop = geneEncoding(pop_size, chrom_length)

for i in range(pop_size):
	obj_value = calobjValue(pop, chrom_length, max_value)        # 个体评价
	best_individual1, best_individual2, best_individual3, best_fit = best(pop, obj_value)		# 第一个存储最优的解, 第二个存储最优基因
	results.append([best_fit, b2d(best_individual1, max_value, chrom_length), b2d(best_individual2, max_value, chrom_length), b2d(best_individual3, max_value, chrom_length)])
	selection(pop, obj_value)		# 新种群复制
	crossover(pop, pc)		# 交配
	mutation(pop, pm)       # 变异

results = results[1:]
results.sort()
print(results[-1])
print(best_individual1, best_individual2, best_individual3)
print(best_fit)
print(obj_value[1])

print(results)

print("max : y = %f, x1 = %f, x2 = %f, x3 = %f" % (results[-1][0], results[-1][1], results[-1][2], results[-1][3]))
print("min : y = %f, x1 = %f, x2 = %f, x3 = %f" % (results[0][0], results[0][1], results[0][2], results[0][3]))

X = []
Y = []
for i in range(100):
	X.append(i)
	t = results[i][0]
	Y.append(t)

plt.plot(X, Y)

plt.show()
