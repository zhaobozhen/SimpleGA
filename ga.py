import matplotlib.pyplot as plt
import math

from calobjValue import calobjValue
from selection import selection
from crossover import crossover
from mutation import mutation
from best import best
from geneEncoding import geneEncoding

print('y = 2 * x1 ^ 2 - 3 * x2 ^ 2 - 4 * x1 + 5 * x2 + x3')


# バイナリシーケンスによって表される値を計算する


def b2d(b, max_value, chrom_length):
	t = 0
	for j in range(len(b)):
		t += b[j] * (math.pow(2, j))
	t = t * max_value / (math.pow(2, chrom_length) - 1)
	return t


pop_size = 1000		# 世代数
max_value = 15      # 遺伝子の最大値
chrom_length = 4		# バイナリシーケンスの長さ
pc = 0.6			# 交叉確率
pm = 0.01           # 突然変異確率
max_results = [[]]		# 世代ごとの最大解を保存
min_results = [[]]		# 世代ごとの最小解を保存
fit_value = []		# 個体適応度
fit_mean = []		# 平均適応度

# pop = [[0, 1, 0, 1] for i in range(pop_size)]
pop = geneEncoding(pop_size, chrom_length)

for i in range(pop_size):
	obj_value = calobjValue(pop, chrom_length, max_value)        # 個体評価
	max_indi1, max_indi2, max_indi3, max_fit, min_indi1, min_indi2, min_indi3, min_fit = best(pop, obj_value)
	max_results.append([max_fit, b2d(max_indi1, max_value, chrom_length), b2d(max_indi2, max_value, chrom_length), b2d(max_indi3, max_value, chrom_length)])
	min_results.append([min_fit, b2d(min_indi1, max_value, chrom_length), b2d(min_indi2, max_value, chrom_length), b2d(min_indi3, max_value, chrom_length)])
	selection(pop, obj_value)		# 新しい個体群をコピー
	crossover(pop, pc)		# 交叉
	mutation(pop, pm)       # 突然変異

max_results = max_results[1:]
max_results.sort()
min_results = min_results[1:]
min_results.sort()
print(max_results[-1])
print(min_results[0])

print("max : y = %f, x1 = %f, x2 = %f, x3 = %f" % (max_results[-1][0], max_results[-1][1], max_results[-1][2], max_results[-1][3]))
print("min : y = %f, x1 = %f, x2 = %f, x3 = %f" % (min_results[0][0], min_results[0][1], min_results[0][2], min_results[0][3]))

X = []
Y = []
for i in range(500):
	X.append(i)
	t = max_results[i][0]
	Y.append(t)

plt.plot(X, Y)

plt.show()

X = []
Y = []
for i in range(1000):
	X.append(i)
	t = min_results[i][0]
	Y.append(t)

plt.plot(X, Y)

plt.show()