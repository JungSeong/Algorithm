import sys
input = sys.stdin.readline

N = int(input())
P = 1000000000
dp = [[0]*10 for _ in range(N+1)]

for i in range(1, 10) :
    dp[1][i] = 1

if N >= 2 :
    for n in range(2, N+1) :
        for i in range(10) :
            if i != 0 and i != 9 :
                dp[n][i] += dp[n-1][i-1] % P
                dp[n][i] += dp[n-1][i+1] % P
            elif i == 9 :
                dp[n][i] = dp[n-1][i-1] % P
            elif i == 0 :
                dp[n][i] = dp[n-1][i+1] % P

print(sum(dp[-1]))