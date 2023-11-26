#LEXF - Enumerating k-mers Lexicographically by Teodora Kovacevic

from itertools import product
 
alphabet = list("ABCD")
n = 4

def product_fun(alphabet, n):
    strings = [''.join(p) for p in product(alphabet, repeat=n)]
    sort_str = sorted(strings)
    return sort_str

result = product_fun(alphabet, n)
for s in result:
    print(s)
