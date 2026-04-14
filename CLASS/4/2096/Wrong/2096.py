import sys
input = sys.stdin.readline

N = int(input())
b = [list(map(int, input().split())) for _ in range(N)]
dp_max = [[-float('inf')]*N for _ in range(N)]
dp_min = [[-float('inf')]*N for _ in range(N)]

dp_max[0] = b[0]
dp_min[0] = b[0]

for i in range(1, N) :
    for j in range(N) :
        if j == 0 :
            dp_max[i][j] = max(dp_max[i-1][j], dp_max[i-1][j+1]) + b[i][j]
            dp_min[i][j] = min(dp_min[i - 1][j], dp_min[i - 1][j + 1]) + b[i][j]
        elif j == N-1 :
            dp_max[i][j] = max(dp_max[i-1][j-1], dp_max[i-1][j]) + b[i][j]
            dp_min[i][j] = min(dp_min[i-1][j-1], dp_min[i-1][j]) + b[i][j]
        else :
            dp_max[i][j] = max(dp_max[i-1][j-1], dp_max[i-1][j], dp_max[i-1][j+1]) + b[i][j]
            dp_min[i][j] = min(dp_min[i-1][j-1], dp_min[i-1][j], dp_min[i-1][j+1]) + b[i][j]

print(f"{max(dp_max[-1])} {min(dp_min[-1])}")