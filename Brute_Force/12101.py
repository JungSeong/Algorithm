import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[] for _ in range(n+1)]

for i in range(n+1) :
    if i == 0 :
        dp[i].append("0")
    elif i == 1 :
        dp[i].append("1")
    elif i == 2 :
        dp[i].append(str(dp[i-1][0]) + "+1")
        dp[i].append("2")
    elif i == 3 :
        for j in range(len(dp[i-1])) :
            dp[i].append(str(dp[i-1][j]) + "+1")
        dp[i].append(str(dp[i-2][0]) + "+2")
        dp[i].append("3")
    else :
        for j in range(len(dp[i-1])) :
            dp[i].append(str(dp[i-1][j]) + "+1")
        for j in range(len(dp[i-2])) :
            dp[i].append(str(dp[i-2][j]) + "+2")
        for j in range(len(dp[i-3])) :
            dp[i].append(str(dp[i-3][j]) + "+3")

final_arr = dp[-1]
final_arr.sort()

if k-1 < len(final_arr) :
    print(final_arr[k-1])
else :
    print(-1)