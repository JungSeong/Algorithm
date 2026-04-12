import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(set(map(int, input().split())))

for comb in combinations_with_replacement(nums, M) :
    print(*comb)