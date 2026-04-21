import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N = int(input())
d = defaultdict(list)

for i in range(N-1) :
    p, q = map(int, input().split())
    d[p].append(q)
    d[q].append(p)

visited = [False]*(N+1)
answer = [0]*(N+1)

def BFS() :
    dq = deque()
    dq.append(1)
    visited[1] = True

    while dq :
        cur = dq.popleft()

        for val in d[cur] :
            if not visited[val] :
                visited[val] = True
                dq.append(val)
                answer[val] = cur

BFS()
for elem in answer[2:] :
    print(elem)