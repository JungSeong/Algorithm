import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
l = list(list(map(int, input().split())) for _ in range(N**2))
d = defaultdict()

m = [[0]*N for _ in range(N)]

for elem in l :
    student = elem[0]
    liked_students = elem[1:]
    candidates = []
    d[student] = liked_students

    for r in range(N) :
        for c in range(N) :
            if m[r][c] == 0 :
                cur_r, cur_c = r, c
                lcnt, bcnt = 0, 0
                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)] :
                    new_r, new_c = cur_r+dr, cur_c+dc
                    if 0<=new_r<N and 0<=new_c<N :
                        if m[new_r][new_c] in liked_students :
                            lcnt += 1
                        elif m[new_r][new_c] == 0 :
                            bcnt += 1
                
                candidates.append((-lcnt, -bcnt, r, c))

    candidates.sort()
    sel_r, sel_c = candidates[0][2], candidates[0][3]
    m[sel_r][sel_c] = student

answer = 0
grateful = {0 :0, 1 :1, 2 :10, 3 :100, 4:1000}

for r in range(N) :
    for c in range(N) :
        student = m[r][c]
        liked_students = d[student]

        cnt = 0
        cur_r, cur_c = r, c
        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)] :
            new_r, new_c = cur_r+dr, cur_c+dc
            if 0<=new_r<N and 0<=new_c<N and m[new_r][new_c] in liked_students :
                cnt += 1
        answer += grateful[cnt]

print(answer)