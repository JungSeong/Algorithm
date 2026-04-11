import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
b = list(list(map(int, input().split())) for _ in range(N))
d = defaultdict(list)

for i in range(N) :
    for j in range(N) :
        if b[i][j] == 1 :
            d[i].append(j)

answer = [[0]*N for _ in range(N)]

for i in range(N) :
    dq = deque([i])
    # visited = {}
    visited = {-1}

    while dq :
        cur = dq.popleft()
        for elem in d[cur] :
            if elem not in visited :
                answer[i][elem] = 1
                dq.append(elem)
                visited.add(elem)

for row in answer :
    row = map(str, row)
    print(' '.join(row))