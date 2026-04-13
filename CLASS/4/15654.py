import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = []

for perm in sorted(permutations(nums, M)):
    print(*perm)