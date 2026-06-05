# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.
temp = [[0]*4 for _ in range(4)]
b = [[False]*4 for _ in range(4)]

def answer(temp) :
    for row in temp :
        print(" ".join(map(str, row)))

if dir == 'U' :
    for j in range(4) :
        start = 0
        for i in range(4) :
            if grid[i][j] != 0 :
                if temp[start][j] == grid[i][j] and not b[start][j] :
                    temp[start][j] += grid[i][j]
                    b[start][j] = True
                else :
                    if temp[start][j] == 0 :
                        temp[start][j] = grid[i][j]
                    else :
                        start += 1
                        if temp[start][j] == 0 :
                            temp[start][j] = grid[i][j]
elif dir == 'D' :
    for j in range(4) :
        start = 3
        for i in range(4-1, -1, -1) :
            if grid[i][j] != 0 :
                if temp[start][j] == grid[i][j] and not b[start][j] :
                    temp[start][j] += grid[i][j]
                    b[start][j] = True
                else :
                    if temp[start][j] == 0 :
                        temp[start][j] = grid[i][j]
                    else :
                        start -= 1
                        if temp[start][j] == 0 :
                            temp[start][j] = grid[i][j]
elif dir == 'L' :
    for i in range(4) :
        start = 0
        for j in range(4) :
            if grid[i][j] != 0 : 
                if temp[i][start] == grid[i][j] and not b[i][start] :
                    temp[i][start] += grid[i][j]
                    b[i][start] = True
                else :
                    if temp[i][start] == 0 :
                        temp[i][start] = grid[i][j]
                    else :
                        start += 1
                        if temp[i][start] == 0 :
                            temp[i][start] = grid[i][j]
elif dir == 'R' :
    for i in range(4) :
        start = 3
        for j in range(4-1, -1, -1) :
            if grid[i][j] != 0 :
                if temp[i][start] == grid[i][j] and not b[i][start] :
                    temp[i][start] += grid[i][j]
                    b[i][start] = True
                else :
                    if temp[i][start] == 0 :
                        temp[i][start] = grid[i][j]
                    else :
                        start -= 1
                        if temp[i][start] == 0 :
                            temp[i][start] = grid[i][j]

answer(temp)