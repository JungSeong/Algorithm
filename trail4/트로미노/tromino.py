n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# Please write your code here.
for i in range(n) :
    for j in range(m) :
        possible = []
        for op in range(6) :
            if op == 0 :
                if 0<=i+2<n and 0<=j<m :
                    possible.append(sum([grid[i][j], grid[i+1][j], grid[i+2][j]]))
            elif op == 1 :
                if 0<=i<n and 0<=j+2<m :
                    possible.append(sum([grid[i][j], grid[i][j+1], grid[i][j+2]]))
            elif op == 2 :
                if 0<=i+1<n and 0<=j+1<m :
                    possible.append(sum([grid[i][j], grid[i+1][j], grid[i+1][j+1]]))
            elif op == 3 :
                if 0<=i-1<n and 0<=j+1<m :
                    possible.append(sum([grid[i][j], grid[i][j+1], grid[i-1][j+1]]))
            elif op == 4 :
                if 0<=i+1<n and 0<=j+1<m :
                    possible.append(sum([grid[i][j], grid[i][j+1], grid[i+1][j+1]]))
            elif op == 5 :
                if 0<=i+1<n and 0<=j+1<m :
                    possible.append(sum([grid[i][j], grid[i+1][j], grid[i][j+1]]))

        if possible :
            comp = max(possible)
            ans = max(ans, comp)

print(ans)