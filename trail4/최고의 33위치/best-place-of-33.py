n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
row, col = 0, 0

for r in range(n-2) :
    for c in range(n-2) :
        cnt = 0
        sel = grid[r:r+3]
        for row in sel :
            cnt += sum(row[c:c+3])

        if max(ans, cnt) == cnt :
            ans = cnt

print(ans)