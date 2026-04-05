import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*10 for _ in range(N+1)]

if N == 1 :
    dp[N] = list(map(lambda x : x+1, dp[N]))
else :
    for i in range(2, N+1) :
        for j in range(10) :
            dp[j:10] = list(map(lambda x : x+1, dp[j:10]))

print(dp)