import sys
from collections import deque
input = sys.stdin.readline

move = [(-1,0), (0,1), (1,0), (0,-1)]
n, m = map(int, input().split())
b = list(list(map(int, input().split())) for _ in range(n))
answer = [[-1]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dq = deque()
start_r, start_c = -1, -1

for i in range(n) :
    for j in range(m) :
        if b[i][j] == 2 :
            dq.append([i, j, 0])
            start_r, start_c = i, j
        elif b[i][j] == 0 :
            answer[i][j] = 0

answer[start_r][start_c] = 0
visited[start_r][start_c] = True

def BFS() :
    while dq :
        cur_r, cur_c, cnt = dq.popleft()

        for dr, dc in move :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<n and 0<=new_c<m and b[new_r][new_c] not in [0, 2] and not visited[new_r][new_c] :
                answer[new_r][new_c] = cnt+1
                visited[new_r][new_c] = True
                dq.append([new_r, new_c, cnt+1])
    return

BFS()

for row in answer :
    row = map(str, row)
    print(' '.join(row))