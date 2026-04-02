import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
visited = [[False]*m for _ in range(n)]
move = [(-1,0), (0,1), (1,0), (0,-1)]

def BFS(cur_r, cur_c) :
    dq = deque()
    dq.append([cur_r, cur_c])
    area = 0

    while dq :
        cur_r, cur_c = dq.popleft()
        area += 1
        visited[cur_r][cur_c] = True
        for dr, dc in move :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<n and 0<=new_c<m and board[new_r][new_c] == 1 and visited[new_r][new_c] == False :
                visited[new_r][new_c] = True
                dq.append([new_r, new_c])

    return area

answer = []

for i in range(n) :
    for j in range(m) :
        if board[i][j] == 1 and visited[i][j] == False :
            area = BFS(i, j)
            answer.append(area)

if answer :
    print(len(answer))
    print(max(answer))
else :
    print(0)
    print(0)