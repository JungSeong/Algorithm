n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
best_area = -1
heights = [0]*m

for i in range(n) :
    for j in range(m) :
        if grid[i][j] > 0 :
            heights[j] += 1
        else :
            heights[j] = 0

    stack = []
    for k in range(m+1) :
        cur_height = heights[k] if k < m else 0
        start = k

        while stack and stack[-1][1] > cur_height :
            r, c = stack.pop()
            best_area = max(best_area, c*(k-r))
            start = r

        stack.append((start, cur_height))

print(best_area)