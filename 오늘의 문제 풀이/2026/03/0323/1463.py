import sys
input = sys.stdin.readline

N = int(input())
dp = [float('inf')]*(N+1)
dp[1] = 0

for i in range(1, N) :
    if i+1<=N :
        dp[i+1] = min(dp[i]+1, dp[i+1])
    if i*2<=N :
        dp[i*2] = min(dp[i]+1, dp[i*2])
    if i*3<=N :
        dp[i*3] = min(dp[i]+1, dp[i*3])

print(dp[-1])