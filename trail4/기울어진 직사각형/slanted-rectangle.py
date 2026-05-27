n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

answer = 0
op = [(-1,1), (-1,-1), (1,-1), (1,1)]

for i in range(2, n) :
    for j in range(1, n-1) :
        for p in range(1, n-1) :
            for q in range(1, n-1) :
                cur_r, cur_c = i, j
                steps = [p,q,p,q]
                isOK = True
                cnt = 0
                
                for k in range(4) :
                    cur_dr, cur_dc = op[k][0], op[k][1]

                    for l in range(1, steps[k]+1) :
                        if 0<=cur_r+l*cur_dr<n and 0<=cur_c+l*cur_dc<n :
                            cnt += grid[cur_r+l*cur_dr][cur_c+l*cur_dc]
                        else :
                            isOK = False
                            break
                    
                    if isOK :
                        cur_r, cur_c = cur_r+cur_dr*steps[k], cur_c+cur_dc*steps[k]
                    else :
                        break

                if isOK :
                    answer = max(answer, cnt)

print(answer)