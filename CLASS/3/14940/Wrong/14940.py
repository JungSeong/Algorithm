import sys
from collections import deque
input = sys.stdin.readline

move = [(-1,0), (0,1), (1,0), (0,-1)]
n, m = map(int, input().split())
b = list(list(map(int, input().split())) for _ in range(n))

def BFS(cur_r, cur_c) :
    dq = deque()
    dq.append([cur_r, cur_c, 0])
    visited = [[False]*m for _ in range(n)]
    visited[cur_r][cur_c] = True

    while dq :
        cur_r, cur_c, cnt = dq.popleft()
        if b[cur_r][cur_c] == 2 :
            return cnt

        for dr, dc in move :
            new_r, new_c = cur_r + dr, cur_c + dc

            if 0<=new_r<n and 0<=new_c<m and not visited[new_r][new_c] :
                visited[new_r][new_c] = True
                dq.append([new_r, new_c, cnt+1])

    return -1

answer = [[0]*m for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        if b[i][j] == 0 or b[i][j] == 2 :
            answer[i][j] = 0
        else :
            answer[i][j] = BFS(i, j)

for row in answer :
    row = map(str, row)
    print(' '.join(row))