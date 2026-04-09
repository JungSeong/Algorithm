import sys, math
input = sys.stdin.readline

n = int(input())
dp = [0] + [float('inf')] * n

for i in range(1, n + 1):
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])