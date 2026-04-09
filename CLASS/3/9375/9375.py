import sys
from collections import defaultdict, Counter

input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    d = defaultdict(list)

    for i in range(n):
        p, q = input().split()
        d[q].append(p)

    answer = 1

    for _, v in d.items() :
        answer = answer * (len(v)+1)

    print(answer-1)