import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
m = list(list(map(int, input().split())) for _ in range(R))

top, bottom = 0, 0

for i in range(R) :
    if m[i][0] == -1 :
        top = i
        bottom = i+1
        break

def air_top() :
    for i in range(top-1, 0, -1) :
        m[i][0] = m[i-1][0] 
    for i in range(C-1) :
        m[0][i] = m[0][i+1]
    for i in range(top) :
        m[i][-1] = m[i+1][-1]
    for i in range(C-1, 1, -1) :
        m[top][i] = m[top][i-1]
    m[top][1] = 0

def air_bottom() :
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
    added_m = [[0]*C for _ in range(R)]
    for i in range(R) :
        for j in range(C) : 
            if m[i][j] > 0 : # 1번 상황
                cur_r, cur_c = i, j
                val = m[i][j] // 5
                cnt = 0
                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)] :
                    new_r, new_c = cur_r + dr, cur_c + dc
                    if 0<=new_r<R and 0<=new_c<C and m[new_r][new_c] != -1 :
                        added_m[new_r][new_c] += val
                        cnt += 1
                added_m[cur_r][cur_c] -= val * cnt
    for i in range(R) :
        for j in range(C) :
            m[i][j] += added_m[i][j]

    air_top()
    air_bottom()

answer = 0

for row in m :
    answer += sum(row)

print(answer+2)