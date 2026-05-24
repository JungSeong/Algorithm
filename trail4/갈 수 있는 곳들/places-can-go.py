n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
from collections import deque
visited = [[False]*n for _ in range(n)]

def BFS() :
    dq = deque()
    answer = 0

    for r, c in points :
        dq.append([r-1, c-1])
        visited[r-1][c-1] = True
        answer += 1

    while dq :
        cur_r, cur_c = dq.popleft()
        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)] :
            new_r, new_c = cur_r + dr, cur_c + dc

            if 0<=new_r<n and 0<=new_c<n and not grid[new_r][new_c] and not visited[new_r][new_c] :
                dq.append([new_r, new_c])
                visited[new_r][new_c] = True
                answer += 1

    return answer

print(BFS())