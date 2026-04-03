import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*2 for _ in range(n)]
arr = []

for i in range(n) :
    s = int(input())
    arr.append(s)

for i in range(n) :
    if i == 0 :
        dp[i][0] = arr[0]
    elif i == 1 :
        dp[i][0] = arr[1]
        dp[i][1] = arr[0] + arr[1]
    else :
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + arr[i]
        dp[i][1] = max(dp[i-1][0], dp[i-2][1]) + arr[i]

answer = -1
for i in range(n) :
    answer = max(answer, max(dp[i][0], dp[i][1]))

print(answer)