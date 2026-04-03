import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*2 for _ in range(N+1)]

for i in range(N) :
    Ti, Pi = map(int, input().split())
    arr[i][0] = Ti
    arr[i][1] = Pi

dp = [0]*(N+1)

for i in range(N-1, -1, -1) :
    Ti, Pi = arr[i][0], arr[i][1]
    if i+Ti > N :
        dp[i] = dp[i+1]
    else :
        dp[i] = max(dp[i+Ti]+Pi, dp[i+1])

print(max(dp))