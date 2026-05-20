n = int(input())

# Please write your code here.
dp = [0]*(n+1)
dp[0] = 1

for i in range(1, n+1) :
    for j in range(1, 5) :
        if i >= j :
            dp[i] += dp[i-j]

print(dp[-1])