import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N = int(input())
dq = deque()

for i in range(N-1) :
    p, q = map(int, input().split())
    dq.append((p, q))

d = defaultdict(list)

def BFS() :
    while dq :
        p, q = dq.popleft()

        if p == 1 and q != 1 :
            d[p].append(q)
        elif p != 1 and q == 1 :
            d[q].append(p)
        else :
            dt = defaultdict(list)
            if d :
                for k, v in d.items() :
                    if p in v :
                        dt[p].append(q)
                    elif q in v :
                        dt[q].append(p)
                    else :
                        dq.append((p, q))
                d += dt
                print(d.items())

BFS()
print(d.items())