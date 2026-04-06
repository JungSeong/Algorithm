import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
dp = [0]*(F+1)
visited = [False]*(F+1)

def BFS(cur_l) :
    dq = deque()
    dq.append([cur_l, 0])

    while dq :
        cur_l, cnt = dq.popleft()
        visited[cur_l] = True

        if cur_l == G :
            return cnt
        for dr in [U, D] :
            if dr == U :
                new_l = cur_l + dr
            else :
                new_l = cur_l - dr

            if 1<=new_l<=F and not visited[new_l] :
                visited[new_l] = True
                dq.append([new_l, cnt+1])

    return "use the stairs"

print(BFS(S))