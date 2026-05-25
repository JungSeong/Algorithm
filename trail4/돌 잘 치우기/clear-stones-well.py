n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Please write your code here.
from itertools import combinations
from collections import deque

locs = []

for i in range(n) :
    for j in range(n) :
        if grid[i][j] :
            locs.append([i, j])

answer = -1

for comb in combinations(locs, m) :
    dq = deque()
    visited = [[False]*n for _ in range(n)]
    cnt = 0

    for i in range(len(r)) :
        cur_r, cur_c = r[i], c[i]
        dq.append([cur_r, cur_c])
        visited[cur_r][cur_c] = True
        cnt += 1

    while dq :
        cur_r, cur_c = dq.popleft()

        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)] :
            new_r, new_c = cur_r + dr, cur_c + dc

            if 0<=new_r<n and 0<=new_c<n and not visited[new_r][new_c] :
                if not grid[new_r][new_c] or [new_r, new_c] in comb :
                    dq.append([new_r, new_c])
                    visited[new_r][new_c] = True
                    cnt += 1

    answer = max(answer, cnt)

print(answer)