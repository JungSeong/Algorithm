import sys
input = sys.stdin.readline

T, W = map(int, input().split())
dp = [[[0]*(W+1) for _ in range(T)] for _ in range(3)]
jado = [0]*T

for t in range(T) :
    jado[t] = int(input())

for t in range(T) :
    if t == 0 :
        dp[1][t][0] = 1 if jado[t] == 1 else 0
    elif t == 1 :
        dp[1][t][0] += dp[1][t-1][0]
        dp[1][t][0] += 1 if jado[t] == 1 else 0
        dp[2][t][1] += dp[1][t-1][0]
        dp[2][t][1] += 1 if jado[t] == 2 else 0
    else :
        for w in range(W+1) :
            if w == 0 :
                dp[1][t][w] += dp[1][t-1][w]
                dp[1][t][w] += 1 if jado[t] == 1 else 0
            else :
                if dp[1][t-1][w] or dp[2][t-1][w-1] :
                    dp[1][t][w] += max(dp[1][t-1][w], dp[2][t-1][w-1])
                    dp[1][t][w] += 1 if jado[t] == 1 else 0
                if dp[2][t-1][w] or dp[1][t-1][w-1]:
                    dp[2][t][w] += max(dp[2][t-1][w], dp[1][t-1][w-1])
                    dp[2][t][w] += 1 if jado[t] == 2 else 0

answer = -1
for i in range(1, 3) :
    answer = max(answer, max(dp[i][-1]))

print(answer)