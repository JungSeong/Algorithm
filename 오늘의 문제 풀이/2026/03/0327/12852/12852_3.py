import sys
input = sys.stdin.readline

N = int(input())
dp = [float('inf')] * (N+1)
oper = [0] * (N+1)
dp[N] = 0

for i in range(N, 1, -1) :
    if dp[i] != float('inf') :
        if i % 3 == 0 :
            if dp[i]+1 < dp[i//3] :
                dp[i//3] = dp[i] + 1
                oper[i//3] = i
        if i % 2 == 0 :
            if dp[i]+1 < dp[i//2] :
                dp[i//2] = dp[i] + 1
                oper[i//2] = i
        if 1<=N-1 :
            if dp[i]+1 < dp[i-1] :
                dp[i-1] = dp[i] + 1
                oper[i-1] = i

print(dp[1])
current = 1
answer = [1]

while current != N :
    current = oper[current]
    answer.append(current)

answer.reverse()
print(*answer)