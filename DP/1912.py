import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

dp = [0]*n
dp[0] = l[0]

for i in range(1, n) :
    dp[i] = max(l[i], dp[i-1]+l[i])

print(max(dp))