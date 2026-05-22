n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
m = [[0]*n for _ in range(n)]
oper = {1: [(-2,0), (-1,0), (0,0), (1,0), (2,0)], 2: [(-1,0), (0,1), (0,0), (1,0), (0,-1)], 3: [(-1,-1), (-1,1), (0,0), (1,1), (1, -1)]}

# Please write your code here.
loc = []

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 1 :
            loc.append([i, j])

def BFS(idx) :
    if idx == len(loc) :
        cnt = 0
        for i in range(n) :
            for j in range(n) :
                if m[i][j] >= 1 :
                    cnt += 1
        return cnt

    answer = 0
    r, c = loc[idx]
    for i in range(1,4) :
        for dr, dc in oper[i] :
            if 0<=r+dr<n and 0<=c+dc<n :
                m[r+dr][c+dc] += 1
        answer = max(answer, BFS(idx+1))
        for dr, dc in oper[i] :
            if 0<=r+dr<n and 0<=c+dc<n :
                m[r+dr][c+dc] -= 1
    
    return answer

print(BFS(0))