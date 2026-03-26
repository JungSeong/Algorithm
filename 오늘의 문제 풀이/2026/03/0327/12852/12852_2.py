import sys
input = sys.stdin.readline

N = int(input())
dp = [[float('inf'), []] for _ in range(N+1)]
dp[N][0] = 0

for i in range(N, 1, -1) :
    if dp[i][0] != float('inf') :
        if i % 3 == 0 :
            if dp[i][0]+1 < dp[i//3][0] :
                dp[i//3][0] = dp[i][0] + 1
                dp[i//3][1].extend(dp[i][1] + [3])
        if i % 2 == 0 :
            if dp[i][0]+1 < dp[i//2][0] :
                dp[i//2][0] = dp[i][0] + 1
                dp[i//2][1].extend(dp[i][1] + [2])
        if 1<=N-1 :
            if dp[i][0]+1 < dp[i-1][0] :
                dp[i-1][0] = dp[i][0] + 1
                dp[i-1][1].extend(dp[i][1] + [-1])

oper = dp[1][1]

answer = N
answer_list = []
answer_list.append(answer)

for elem in oper :
    if elem == 3 :
        answer //= 3
    elif elem == 2 :
        answer //= 2
    else :
        answer -= 1
    answer_list.append(answer)

print(*answer_list)