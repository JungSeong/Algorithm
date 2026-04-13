import sys
from collections import defaultdict
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = defaultdict(int)

for perm in product(nums, repeat=M) :
    answer[tuple(sorted(perm))] += 1

result = answer.keys()
for elem in sorted(result) :
    print(*elem)