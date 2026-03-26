import sys
input = sys.stdin.readline

N = int(input())
dp = [[float('inf'), 0]*(N+1)]
dp[N][0] = 0

for i in range(N, 0, -1) :
    if dp[i][0] != float('inf') :
        if i % 3 == 0 :
            if min(dp[i][0]+1, dp[i//3][0]) == dp[i][0]+1 :
                dp[i//3][0] = dp[i][0] + 1
                dp[i//3][1] = 3
        if i % 2 == 0 :
            if min(dp[i][0]+1, dp[i//2][0]) == dp[i][0]+1 :
                dp[i//2][0] = dp[i][0] + 1
                dp[i//2][1] = 2
        if 1<=N-1 :
            if min(dp[i][0]+1, dp[i-1][0]) == dp[i][0]+1 :
                dp[i-1][0] = dp[i][0] + 1
                dp[i-1][1] = -1

print(dp)