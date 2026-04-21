import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
b = list(list(map(int, input().split())) for _ in range(N))
dp = [[0]*N for _ in range(N)]

oper = ["right", "down", "diag"]

def BFS(cur_r, cur_c) :
    dq = deque()
    dq.append([cur_r, cur_c, "right"])
    dp[0][1] = 1

    while dq :
        cur_r, cur_c, op = dq.popleft()

        if op == "right" :
            if 0<=cur_r<N and 0<=cur_c+1<N and not b[cur_r][cur_c+1] :
                dp[cur_r][cur_c+1] += dp[cur_r][cur_c]
                dq.append([cur_r, cur_c+1, "right"])
            if 0<=cur_r+1<N and 0<=cur_c+1<N and not b[cur_r+1][cur_c] and not b[cur_r+1][cur_c+1] and not b[cur_r][cur_c+1] :
                dp[cur_r+1][cur_c+1] += dp[cur_r][cur_c]
                dq.append([cur_r+1, cur_c+1, "diag"])
        elif op == "down" :
            if 0<=cur_r+1<N and 0<=cur_c<N and not b[cur_r+1][cur_c] :
                dp[cur_r+1][cur_c] += dp[cur_r][cur_c]
                dq.append([cur_r+1, cur_c, "down"])
            if 0<=cur_r+1<N and 0<=cur_c+1<N and not b[cur_r+1][cur_c] and not b[cur_r+1][cur_c+1] and not b[cur_r][cur_c+1] :
                dp[cur_r+1][cur_c+1] += dp[cur_r][cur_c]
                dq.append([cur_r+1, cur_c+1, "diag"])
        else :
            if 0<=cur_r<N and 0<=cur_c+1<N and not b[cur_r][cur_c+1] :
                dp[cur_r][cur_c+1] += dp[cur_r][cur_c]
                dq.append([cur_r, cur_c+1, "right"])
            if 0<=cur_r+1<N and 0<=cur_c<N and not b[cur_r+1][cur_c] :
                dp[cur_r+1][cur_c] += dp[cur_r][cur_c]
                dq.append([cur_r+1, cur_c, "down"])
            if 0<=cur_r+1<N and 0<=cur_c+1<N and not b[cur_r+1][cur_c] and not b[cur_r+1][cur_c+1] and not b[cur_r][cur_c+1] :
                dp[cur_r+1][cur_c+1] += dp[cur_r][cur_c]
                dq.append([cur_r+1, cur_c+1, "diag"])

BFS(0, 1)
for row in dp :
    print(row)

print(dp[-1][-1])