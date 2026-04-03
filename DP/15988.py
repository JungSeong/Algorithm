import sys
input = sys.stdin.readline

T = int(input())
p = 1000000009
dp = [0]*1000001

for t in range(T) :
    n = int(input())
    for i in range(n) :
        if i == 0 and dp[i] == 0 :
            dp[0] = 1
        elif i == 1 and dp[i] == 0 :
            dp[1] = 2
        elif i == 2 and dp[i] == 0 :
            dp[2] = 4
        elif i >= 3 and dp[i] == 0 :
            dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % p

    print(dp[n-1])