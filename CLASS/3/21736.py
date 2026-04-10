import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
b = list(list(input().rstrip()) for _ in range(N))
visited = [[False]*M for _ in range(N)]
move = [(-1,0), (0,1), (1,0), (0,-1)]
dq = deque()

for i in range(N) :
    for j in range(M) :
        if b[i][j] == 'I' :
            dq.append((i, j))

def BFS() :
    answer = 0

    while dq :
        cur_r, cur_c = dq.popleft()
        visited[cur_r][cur_c] = True

        for dr, dc in move :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<N and 0<=new_c<M and not visited[new_r][new_c] and b[new_r][new_c] != 'X' :
                visited[new_r][new_c] = True
                if b[new_r][new_c] == 'P' :
                    answer += 1
                dq.append((new_r, new_c))

    if not answer :
        return "TT"
    return answer

print(BFS())