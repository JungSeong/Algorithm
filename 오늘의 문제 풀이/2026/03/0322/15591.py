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
    dq = deque()
    dq.append(v)
    cnt = 0
    visited = [False]*(N+1) # 이미 방문한 노드를 다시 방문하여 재귀에 빠지는 현상을 막기 위함
    visited[v] = True

    while dq :
        v = dq.popleft()
        l = d[v]

        for elem in l :
            if elem[1] >= k and visited[elem[0]] == False :
                visited[elem[0]] = True
                dq.append(elem[0])
                cnt += 1

    print(cnt)                