import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())
board = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]
move = [(-1,0), (0,1), (1,0), (0,-1)]

for i in range (K) :
    sr, sc, er, ec = map(int, input().split())
    for c in range(sc, ec):
        for r in range(sr, er) :
            board[c][r] = 1

def BFS(r, c) :
    visited[r][c] = True
    dq = deque([(r, c)])
    cnt = 1

    while dq :
        cur_r, cur_c = dq.popleft()

        for dr, dc in move :
            new_r, new_c = cur_r+dr, cur_c+dc
            if 0<=new_r<M and 0<=new_c<N and not visited[new_r][new_c] and board[new_r][new_c] != 1 :
                visited[new_r][new_c] = True
                cnt += 1
                dq.append((new_r, new_c))

    return cnt

area = []

for i in range(M) :
    for j in range(N) :
        if not visited[i][j] and board[i][j] == 0 :
            area.append(BFS(i, j))

print(len(area))
area.sort()
area = map(str, area)
print(' '.join(area))