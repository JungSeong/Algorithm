import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = list(list(input().rstrip()) for _ in range(R))
visited = [[False]*C for _ in range(R)]
start_r, start_c = 0, 0
fires = []

for i in range(R) :
    for j in range(C) :
        if board[i][j] == 'J' :
            start_r, start_c = i, j
        elif board[i][j] == 'F' :
            fires.append((i, j))

visited[start_r][start_c] = True
move = [(-1,0), (0,1), (1,0), (0,-1)]

def BFS(cur_r, cur_c) :
    dq = deque([(cur_r, cur_c, 1)])
    global fires

    while dq :
        cur_r, cur_c, cur_time = dq.popleft()
        if cur_r in [0, R-1] or cur_c in [0, C-1] : # 경계선에 닿았을 때
            print(cur_time)
            return

        temp_fires = []
        for floc_r, floc_c in fires :
            for dr, dc in move :
                nfloc_r, nfloc_c = floc_r + dr, floc_c + dc
                if board[nfloc_r][nfloc_c] != '#' :
                    temp_fires.append((nfloc_r, nfloc_c))

        for dr, dc in move :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<R and 0<=new_c<C and not visited[new_r][new_c] and board[new_r][new_c] == '.' :
                board[new_r][new_c] = 'J'
                dq.append((new_r, new_c, cur_time + 1))

        for r, c in temp_fires :
            board[r][c] = 'F'
        fires += temp_fires

    print("IMPOSSIBLE")

BFS(start_r, start_c)