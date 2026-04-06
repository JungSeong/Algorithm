import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
move = [(-1,0), (0,1), (1,0), (0,-1)]

for i in range(T) :
    w, h = map(int, input().split())
    board = list(list(input().rstrip()) for _ in range(h))
    people_q = deque()
    fire_q = deque()
    visited = [[False]*w for _ in range(h)]

    for i in range(h) :
        for j in range(w) :
            print(f"{i} {j}")
            if board[i][j] == "@" :
                people_q.append((i, j, 0))
            elif board[i][j] == "*" :
                fire_q.append((i, j))

    def BFS() :
        while fire_q :
            for i in range(len(fire_q)) :
                cur_r, cur_c = fire_q.popleft()
                for dr, dc in move :
                    new_r, new_c = cur_r + dr, cur_c + dc
                    if 0<=new_r<h and 0<=new_c<w and board[new_r][new_c] != "#" :
                        board[new_r][new_c] = "*"
                        fire_q.append((new_r, new_c))

        while people_q :
            for i in range(len(people_q)) :
                cur_r, cur_c, cnt = people_q.popleft()
                for dr, dc in move :
                    new_r, new_c = cur_r + dr, cur_c + dc
                    if new_r in [0, h-1] and new_c in [0, w-1] :
                        print(cnt+1)
                        return

                    if 0<=new_r<h and 0<=new_c<w and not visited[new_r][new_c] and board[new_r][new_c] not in ["#", "*"] :
                        visited[new_r][new_c] = True
                        people_q.append((new_r, new_c, cnt+1))
            print("IMPOSSIBLE")

    BFS()