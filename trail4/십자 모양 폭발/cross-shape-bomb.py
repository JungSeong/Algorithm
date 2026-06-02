n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
r, c = r-1, c-1
num = grid[r][c]

for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)] :
    cr, cc = r, c
    for i in range(num-1) :
        nr, nc = cr+dr, cc+dc
        if 0<=nr<n and 0<=nc<n :
            grid[nr][nc] = -1
            cr, cc = nr, nc
        else :
            break

grid[r][c] = -1

temp = [[0]*n for _ in range(n)]

for j in range(n) :
    I = n-1
    for i in range(n-1, -1, -1) :
        if not grid[i][j] == -1 :
            temp[I][j] = grid[i][j]
            I -= 1

for row in temp :
    print(" ".join(map(str, row)))