import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, Q = map(int, input().split())
d = defaultdict(list)

for i in range(N-1) :
    p, q, r = map(int, input().split())
    d[p].append((q, r))
    d[q].append((p, r))

for i in range(Q) :
    k, v = map(int, input().split())
    dq = deque([v])
    visited = [False] * (N+1)
    visited[v] = True
    cnt = 0

    while dq :
        cur_k = dq.popleft()
        for u, usado in d[cur_k] :
            if usado >= k and not visited[u]:
                dq.append(u)
                visited[u] = True
                cnt += 1

    print(cnt)
