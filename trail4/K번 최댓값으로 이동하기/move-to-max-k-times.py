n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
from collections import deque
r, c = r-1, c-1

for K in range(k-1, -1, -1) :
    dq = deque()
    dq.append([r, c])
    threshold = grid[r][c]
    visited = [[False]*n for _ in range(n)]
    visited[r][c] = True
    candidates = []

    while dq :
        cur_r, cur_c = dq.popleft()

        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)] :
            new_r, new_c = cur_r + dr, cur_c + dc

            if 0<=new_r<n and 0<=new_c<n and grid[new_r][new_c] < threshold and not visited[new_r][new_c] :
                dq.append([new_r, new_c])
                visited[new_r][new_c] = True
                candidates.append([new_r, new_c, grid[new_r][new_c]])

    if len(candidates) == 0 :
        break

    candidates.sort(key=lambda x : (-x[2], x[0], x[1]))
    r, c = candidates[0][0], candidates[0][1]

print(f"{r+1} {c+1}")