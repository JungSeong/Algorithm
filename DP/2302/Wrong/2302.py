import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
vips = set()

for i in range(M) :
    v = int(input())
    vips.add(v)

l = list(range(1, N+1))
lengths = []
len = 0

for i in range(1, N+1) :
    if i in vips and len != 0 :
        lengths.append(len)
        len = 0
        continue
    len += 1

if len >= 0 :
    lengths.append(len)

dp = [[0]*2 for _ in range(N+1)]
answer = 1

dp[1][0] = dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 2

for len in lengths :
    for i in range(len, N+1) :
        if dp[i][0] == 0 or dp[i][1] == 0 :
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]

    answer *= sum(dp[len-1])

print(answer)