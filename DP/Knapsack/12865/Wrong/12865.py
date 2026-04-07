import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0]*(K+1)

for i in range(N) :
    Wi, Vi = map(int, input().split())
    dp[Wi] = Vi

for i in range(K-1, 0, -1) :
    dp[K] = max(dp[K], dp[i] + dp[K-i])

print(dp[-1])