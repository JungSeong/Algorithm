import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)

for i in range(1, N+1) :
    if i == 1 :
        dp[i] = 0
    else :
        dp[i] = dp[i-1] + 1
        if i%2==0 :
            dp[i] = min(dp[i//2]+1, dp[i])
        if i%3==0 :
            dp[i] = min(dp[i//3]+1, dp[i])

print(dp[-1])