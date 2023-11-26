#CUNR - Counting Unrooted Binary Trees by Teodora Kovacevic

from functools import reduce

n = 934
print(reduce(lambda a, b: a * b % 10**6, range(2 * n - 5, 1, -2)))
