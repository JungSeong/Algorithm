K, N = map(int, input().split())

# Please write your code here.
from itertools import product
l = range(1, K+1)

for comb in product(l, repeat=N) :
    print(" ".join(map(str, comb)))