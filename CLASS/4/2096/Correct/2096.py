import sys
input = sys.stdin.readline

N = int(input())
b = [list(map(int, input().split())) for _ in range(N)]

dp_max = b[0]
dp_min = b[0]

temp_max = [0]*3
temp_min = [0]*3

for i in range(1, N) :
    for j in range(3) :
        if j == 0 :
            temp_max[j] = max(dp_max[j], dp_max[j+1]) + b[i][j]
            temp_min[j] = min(dp_min[j], dp_min[j+1]) + b[i][j]
        elif j == 1 :
            temp_max[j] = max(dp_max[j-1], dp_max[j], dp_max[j+1]) + b[i][j]
            temp_min[j] = min(dp_min[j-1], dp_min[j], dp_min[j+1]) + b[i][j]
        elif j == 2 :
            temp_max[j] = max(dp_max[j-1], dp_max[j]) + b[i][j]
            temp_min[j] = min(dp_min[j-1], dp_min[j]) + b[i][j]

    dp_max = temp_max[:]
    dp_min = temp_min[:]

print(f"{max(dp_max)} {min(dp_min)}")