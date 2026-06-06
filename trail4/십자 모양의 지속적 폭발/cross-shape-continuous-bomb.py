n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

# Please write your code here.
for j in commands :
    j = j-1
    temp = [[0]*n for _ in range(n)]
    num = 0

    for i in range(n) :
        if grid[i][j] != 0 :
            num = grid[i][j]
            num -= 1
            ii, ij = i, j
            break

    for c in range(n) :
        cnt = n-1
        for r in range(n-1, -1, -1) :
            if (c==ij and ii-num<=r<=ii+num) or (r==ii and ij-num<=c<=ij+num) :
                continue
            else :
                temp[cnt][c] = grid[r][c]
                cnt -= 1

    grid[:] = temp
                
for row in grid :
    print(" ".join(map(str, row)))