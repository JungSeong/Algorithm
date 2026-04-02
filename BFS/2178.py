import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
b = list(list(map(int, input().rstrip())) for _ in range(N))
visited = [[False]*M for _ in range(N)]

def BFS(cur_r, cur_c) :
    dq = deque([(cur_r, cur_c)])

    while dq :
        cur_r, cur_c = dq.popleft()
        if cur_r == N-1 and cur_c == M-1 :
            print(b[cur_r][cur_c])
            return
        for dr, dc in [(-1,0), (0,1), (1,0), (0, -1)] :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<N and 0<=new_c<M and visited[new_r][new_c] == False and b[new_r][new_c] == 1 :
                b[new_r][new_c] = b[cur_r][cur_c] + 1
                dq.append((new_r, new_c))

BFS(0, 0)