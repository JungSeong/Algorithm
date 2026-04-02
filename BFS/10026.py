import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
b = list(list(input().rstrip()) for _ in range(N))
visited = [[False]*N for _ in range(N)]
visited_RGB = [[False]*N for _ in range(N)]
color_map = {'R': ['R', 'G'], 'G': ['R','G'], 'B': ['B']}

def BFS(cur_r, cur_c) :
    color = b[cur_r][cur_c]
    dq = deque([(cur_r, cur_c)])
    visited[cur_r][cur_c] = True

    while dq :
        cur_r, cur_c = dq.popleft()
        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)] :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<N and 0<=new_c<N and not visited[new_r][new_c] and b[new_r][new_c] == color :
                visited[new_r][new_c] = True
                dq.append((new_r, new_c))

    return

def BFS_RGB(cur_r, cur_c) :
    color = b[cur_r][cur_c]
    dq_RGB = deque([(cur_r, cur_c)])
    visited_RGB[cur_r][cur_c] = True

    while dq_RGB :
        cur_r, cur_c = dq_RGB.popleft()
        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)] :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<N and 0<=new_c<N and not visited_RGB[new_r][new_c] and color in color_map[b[new_r][new_c]] :
                visited_RGB[new_r][new_c] = True
                dq_RGB.append((new_r, new_c))

    return

answer, answer_RGB = 0, 0

for i in range(N) :
    for j in range(N) :
        if not visited[i][j] :
            BFS(i, j)
            answer += 1
        if not visited_RGB[i][j] :
            BFS_RGB(i, j)
            answer_RGB += 1

print(f"{answer} {answer_RGB}")