import sys
input = sys.stdin.readline

n = int(input())
abs_n = abs(n)
div = 1000000000

dp = [0]*(2*1000000+1)

def get_idx(idx) :
    return idx + abs_n

dp[0 + abs_n] = 0
dp[1 + abs_n] = 1

if n == 0 :
    idx = get_idx(n)
elif n > 0 :
    for i in range(2, n+1) :
        idx = get_idx(i)
        dp[idx] = (dp[idx-1] + dp[idx-2]) % div
    idx = get_idx(n)
else :
    for i in range(-1, n-1, -1) :
        idx = get_idx(i)
        dp[idx] = (dp[idx+2] - dp[idx+1])
        if dp[idx] >= 0 :
            dp[idx] %= div
        else :
            dp[idx] = (abs(dp[idx]) % div) * -1
    idx = get_idx(n)

answer = dp[idx]
if answer > 0 :
    print(1)
    print(answer % div)
elif answer == 0 :
    print(0)
    print(0)
else :
    print(-1)
    print(abs(answer) % div)

# print(dp)