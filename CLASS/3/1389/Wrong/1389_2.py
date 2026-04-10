import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())
d = defaultdict(list)

for i in range(M) :
    p, q = map(int, input().split())
    d[p].append(q)
    d[q].append(p)

result = [0] + [0]*N

for i in range(1, N+1) :
    answer = 0
    for j in range(1, N+1) :
        cnt = 1
        visited = {j}
        if j != i :
            dq = deque()
            for elem in d[i] :
                dq.append((elem, 1))
                visited.add(elem) # PROBLEM!!
            while dq :
                cur, cnt = dq.popleft()
                if cur == j :
                    answer += cnt
                    break
                else :
                    for elem in d[cur] :
                        if elem not in visited :
                            visited.add(elem)
                            dq.append((elem, cnt+1))
    
    result[i] = answer

idx, num = -1, float('inf')
print(result)

for i in range(1, N+1) :
    if result[i] < num :
        num = result[i]
        idx = i

print(idx)