import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
vips = set()

for i in range(M) :
    v = int(input())
    vips.add(v)

lengths = []
curr_len = 0

for i in range(1, N+1) :
    if i in vips :
        if curr_len > 0 :
            lengths.append(curr_len)
            curr_len = 0
    else :
        curr_len += 1

if curr_len > 0 :
    lengths.append(curr_len)

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1
answer = 1

for len in lengths :
    for i in range(2, len+1) :
        if dp[i] == 0 :
            dp[i] = dp[i-1] + dp[i-2]

    answer *= dp[len]

print(answer)