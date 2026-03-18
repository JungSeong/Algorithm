import sys
from collections import deque
input = sys.stdin.readline

R, C, T = map(int, input().split())
m = list(list(map(int, input().split())) for _ in range(R))
move = [(-1,0), (0,1), (1,0), (0,-1)]

for i in range(R) :
    if min(m[i]) == -1 :
        top, bottom = i, i+1
        break

def clean_top(top) :
    for i in range(top-1, 0, -1) :
        m[i][0] = m[i-1][0]
    for i in range(C-1) :
        m[0][i] = m[0][i+1]
    for i in range(top) :
        m[i][-1] = m[i+1][-1]
    for i in range(C-1, 1, -1) :
        m[top][i] = m[top][i-1]
    m[top][1] = 0

def clean_bottom(bottom) :
    for i in range(bottom+1, R-1) :
        m[i][0] = m[i+1][0]
    for i in range(C-1) :
        m[-1][i] = m[-1][i+1]
    for i in range(R-1, bottom, -1) :
        m[i][-1] = m[i-1][-1]
    for i in range(C-1, 1, -1) :
        m[bottom][i] = m[bottom][i-1]
    m[bottom][1] = 0

for t in range(T) :
    # 1번 로직 
    added_dust = [[0]*C for _ in range(R)]
    for i in range(R) :
        for j in range(C) :
            cur = m[i][j]
            if cur > 0 :
                cnt = 0
                for dr, dc in move :
                    new_r, new_c = i+dr, j+dc
                    if 0<=new_r<R and 0<=new_c<C and m[new_r][new_c] != -1 :
                        cnt += 1
                        added_dust[new_r][new_c] += cur//5
                added_dust[i][j] -= (cur//5)*cnt
    
    for i in range(R) :
        for j in range(C) :
            m[i][j] += added_dust[i][j]
    
    # 2번 로직 구현
    clean_top(top)
    clean_bottom(bottom)

answer = 0
for row in m :
    answer += sum(row)

print(answer+2)