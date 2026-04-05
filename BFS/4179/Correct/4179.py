import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = list(list(input().rstrip()) for _ in range(R))

visited = [[False]*C for _ in range(R)]
start_r, start_c = 0, 0

people_q = deque()
fire_q = deque()

for i in range(R) :
    for j in range(C) :
        if board[i][j] == 'J' :
            start_r, start_c = i, j
            people_q.append((i, j, 1))
        elif board[i][j] == 'F' :
            fire_q.append((i, j))

visited[start_r][start_c] = True
move = [(-1,0), (0,1), (1,0), (0,-1)]

def BFS() :
    while people_q :
        for i in range(len(fire_q)) :
            fcur_r, fcur_c = fire_q.popleft()
            for dr, dc in move :
                fnew_r, fnew_c = fcur_r + dr, fcur_c + dc
                if 0<=fnew_r<R and 0<=fnew_c<C and board[fnew_r][fnew_c] not in ["#", "F"] :
                    board[fnew_r][fnew_c] = "F"
                    fire_q.append((fnew_r, fnew_c))

        for i in range(len(people_q)) :
            cur_r, cur_c, cur_time = people_q.popleft()
            if cur_r in [0, R - 1] or cur_c in [0, C - 1]:  # 경계선에 닿았을 때
                print(cur_time)
                return

            for dr, dc in move :
                new_r, new_c = cur_r + dr, cur_c + dc
                if 0<=new_r<R and 0<=new_c<C and not visited[new_r][new_c] and board[new_r][new_c] == '.' :
                    visited[new_r][new_c] = True
                    people_q.append((new_r, new_c, cur_time + 1))

    print("IMPOSSIBLE")

BFS()