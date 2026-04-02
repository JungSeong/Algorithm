import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*2 for _ in range(N+1)]
for i in range(1, N+1):
    Ti, Pi = map(int, input().split())
    arr[i][0], arr[i][1] = Ti, Pi

dp = [0]*(N+2)

for i in range(1, N+1) :
    Ti, Pi = arr[i][0], arr[i][1]
    dp[i+1] = max(dp[i], dp[i+1])

    if i + Ti <= N+1 :
        dp[i+Ti] = max(dp[i]+Pi, dp[i+Ti])

print(dp[-1])