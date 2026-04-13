import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nodes = []

for i in range(N-1) :
    A, B = list(map(int, input().split()))
    nodes.append([A, B])

dq = deque(nodes)
d = dict()

while dq :
    p, q = dq.popleft()

    if p not in d.keys() and q in d.keys() :
        d[q] = p
    elif p in d.keys() and q not in d.keys() :
        d[p] = q