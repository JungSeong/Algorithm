import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = set()

for perm in permutations(nums, M) :
    answer.add(perm)

answer = sorted(answer)
for elem in answer :
    print(*elem)