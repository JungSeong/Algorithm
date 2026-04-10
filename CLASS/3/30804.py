import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

count = defaultdict(int)
left = 0
answer = -float('inf')

for right in range(N) :
    count[S[right]] += 1

    while len(count) > 2 :
        count[S[left]] -= 1

        if count[S[left]] == 0 :
            del count[S[left]]
        left += 1

    answer = max(answer, right-left+1)

print(answer)