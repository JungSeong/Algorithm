n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

def pool(r, c) :
    cnt, s = 1, a[r][c]
    for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)] :
        nr, nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<m :
            cnt += 1
            s += a[nr][nc]
    
    v[r][c] = s // cnt

for Q in range(q) :
    r1, c1, r2, c2 = winds[Q]
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

    t1 = a[r1][c2]
    for p in range(c2, c1, -1) :
        a[r1][p] = a[r1][p-1]
    a[r1][c1] = a[r1+1][c1]
    
    t2 = a[r2][c2]
    for p in range(r2, r1, -1) :
        a[p][c2] = a[p-1][c2]
        if p == r1+1 :
            a[p][c2] = t1
    
    t3 = a[r2][c1]
    for p in range(c1, c2) :
        a[r2][p] = a[r2][p+1]
        if p == c2-1 :
            a[r2][p] = t2

    for p in range(r1, r2) :
        a[p][c1] = a[p+1][c1]
        if p == r2-1 :
            a[p][c1] = t3

    for r in range(r1, r2+1) :
        for c in range(c1, c2+1) :
            pool(r, c)

    for i in range(n) :
        for j in range(m) :
            if r1<=i<=r2 and c1<=j<=c2 :
                a[i][j] = v[i][j]

for row in a :
    print(" ".join(map(str, row)))