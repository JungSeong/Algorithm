import sys
input = sys.stdin.readline

N = int(input())
steps = [0]*(N+1)
dp = [[0]*3 for _ in range(N+1)]

for i in range(1, N+1) :
    step = int(input())
    steps[i] = step

for i in range(1, N+1) :
    if i == 1 :
        dp[i][1] = steps[i] # 연속적으로 밟은 계단이 1개
    elif i == 2 :
        dp[i][1] = steps[i]
        dp[i][2] = steps[i-1] + steps[i] # 연속적으로 밟은 계단이 2개
    else :
        dp[i][1] = max(dp[i-2][1] + steps[i], dp[i-2][2] + steps[i]) # 두 칸 전에서 온 모든 경우가 정답
        dp[i][2] = dp[i-1][1] + steps[i]

answer = max(dp[-1][1], dp[-1][2])

print(answer)