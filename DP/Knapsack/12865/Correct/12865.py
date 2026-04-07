import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0]*(K+1)

for i in range(N) :
    Wi, Vi = map(int, input().split())
    for j in range(K, Wi-1, -1) :
        dp[j] = max(dp[j], dp[j-Wi]+Vi)

print(dp[-1])