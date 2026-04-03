import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
l = list()

for i in range(N**2) :
    kv = list(map(int, input().split()))
    k = kv[0]
    v = kv[1:]
    l.append([k, v])

m = [[0]*N for _ in range(N)]
cal = [[0]*N for _ in range(N)]

def sol(student, liked_students) :
    for i in range(N) :
        for j in range(N) :
            cur_r, cur_c = i, j
            cnt = 0
            for dr, dc in [[-1,0], [0,1], [1,0], [0,-1]] :
                new_r, new_c = cur_r + dr, cur_c + dc
                if 0<=new_r<N and 0<=new_c<N and m[new_r][new_c] in liked_students :
                    cnt += 1
            cal[i][j] = cnt
    
    # 1번 로직 구현
    max_cnt = 0
    most_liked = []
    for i in range(N) :
        for j in range(N) :
            if cal[i][j] > max_cnt :
                max_cnt = cal[i][j]
    
    for i in range(N) :
        for j in range(N) :
            if cal[i][j] == max_cnt :
                most_liked.append([i, j])

    if len(most_liked) == 1 :
        i, j = most_liked[0][0], most_liked[0][1]
        m[i][j] = student
        return
    else : # 2번 로직 구현
        for i in range(len(most_liked)) :
            cur_r, cur_c = most_liked[i][0], most_liked[i][1]
            cnt = 0
            for dr, dc in [[-1,0], [0,1], [1,0], [0,-1]] :
                new_r, new_c = cur_r + dr, cur_c + dc
                if 0<=new_r<N and 0<=new_c<N and m[new_r][new_c] == 0 :
                    cnt += 1
            most_liked[i].extend([cnt])
    
    max_cnt = 0
    for i in range(len(most_liked)) :
        if max_cnt < most_liked[i][-1] :
            max_cnt = most_liked[i][-1]

    second = []

    for i in range(len(most_liked)) :
        if most_liked[i][-1] == max_cnt :
            second.append(most_liked[i])

    if len(second) == 1 :
        i, j = second[0][0], second[0][1]
        m[i][j] = student
        return
    else : # 3번 로직 구현
        min_r, min_c = N, N
        for elem in second :
            r = elem[0]
            if r <= min_r :
                min_r = r
        cnt = 0
        third = []
        for i in range(len(second)) :
            r = second[i][0]
            if r == min_r :
                third.append(second[i])

        print(third)
        
        if len(third) == 1 :
            i, j = third[0][0], third[0][1]
            m[i][j] = student
            return
        else :
            for elem in third :
                c = elem[1]
                if c <= min_c :
                    min_c = c

            last = []
            for i in range(len(third)) :
                c = third[i][1]
                if c == min_c :
                    last.append(third[i])
            
            i, j = last[0][0], last[0][1]
            m[i][j] = student
            return

for elem in l :
    student, liked_student = elem[0], elem[1]
    sol(student, liked_student)
    for row in m :
        print(row)