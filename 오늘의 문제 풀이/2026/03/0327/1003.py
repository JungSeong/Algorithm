import sys
input = sys.stdin.readline

T = int(input())
dp = [[0]*2 for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1

for t in range(T) :
    N = int(input())
    for i in range(2, N+1) :
        if dp[i][0] >= 1 or dp[i][1] >= 1 :
            continue
        else :
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]
    
    print(f"{dp[N][0]} {dp[N][1]}")