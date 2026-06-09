n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
answer = []
cr, cc = r, c

while True :
    num = a[cr][cc]
    answer.append(num)
    isPossible = False

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)] :
        nr, nc = cr+dr, cc+dc

        if 1<=nr<=n and 1<=nc<=n and num<a[nr][nc] :
            cr, cc = nr, nc
            isPossible = True
            break

    if not isPossible :
        break

print(" ".join(map(str, answer)))