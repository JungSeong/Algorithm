import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*10 for _ in range(N+1)]

dp[1] = list(map(lambda x : x+1, dp[1]))
for i in range(2, N+1) :
    for j in range(10) :
        for k in range(j, 10) :
            dp[i][k] += dp[i-1][j]

print(sum(dp[-1]) % 10007)