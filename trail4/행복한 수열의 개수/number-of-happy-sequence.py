n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# Please write your code here.
from itertools import groupby

def cnt(grid, m) :
    ans = 0
    for row in grid :
        for _, group in groupby(row) :
            if len(list(group)) >= m :
                ans += 1
                break
    
    return ans

ans += cnt(grid, m)
rgrid = list(map(list, zip(*grid)))
ans += cnt(rgrid, m)

print(ans)