n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# Please write your code here.
from collections import deque

def BFS() :
    dq = deque()
    dq.append([0, 0])
    visited[0][0] = True

    while dq :
        cur_r, cur_c = dq.popleft()

        if cur_r == n-1 and cur_c == m-1 :
            return 1

        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)] :
            new_r, new_c = cur_r + dr, cur_c + dc

            if 0<=new_r<n and 0<=new_c<m and a[new_r][new_c] and not visited[new_r][new_c] :
                dq.append([new_r, new_c])
                visited[new_r][new_c] = True
    
    return 0

print(BFS())