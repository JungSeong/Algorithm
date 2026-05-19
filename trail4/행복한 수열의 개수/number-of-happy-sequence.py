n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
from collections import Counter

def cnt(grid) :
    ans = 0
    for row in grid :
        length = len(row)
        cnt = 0
        before = -1
        for i in range(length) :
            if before != row[i] :
                cnt = 1
                before = row[i]
            else :
                cnt += 1
            
            if cnt >= m :
                ans += 1
                break

    return ans

ans += cnt(grid)
rgrid = [row for row in map(list, zip(*grid))]
ans += cnt(rgrid)
print(ans)