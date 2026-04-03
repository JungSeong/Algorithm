import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*3 for _ in range(n)]
arr = []

for i in range(n) :
    s = int(input())
    arr.append(s)

for i in range(n) :
    if i == 0 :
        dp[i][1] = arr[0]
    elif i == 1 :
        dp[i][0] = arr[0]
        dp[i][1] = arr[1]
        dp[i][2] = arr[0]+arr[1]
    else :
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) # max로 이게 될껄?
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + arr[i]
        dp[i][2] = dp[i-1][1] + arr[i]

answer = -1
for i in range(n) :
    answer = max(answer, max(dp[i]))

print(answer)