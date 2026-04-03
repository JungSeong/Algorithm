import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*n
arr = []

for i in range(n) :
    s = int(input())
    arr.append(s)

for i in range(n) :
    if i == 0 :
        dp[i] = arr[0]
    elif i == 1 :
        dp[i] = arr[0] + arr[1]
    else :
        dp[i] = max(dp[i-2]+arr[i], dp[i-1], arr[i]+arr[i-1]+dp[i-3]) # 그냥 넘겨 받기

print(dp[-1])