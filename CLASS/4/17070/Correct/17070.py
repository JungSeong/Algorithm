import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
b = list(list(map(int, input().split())) for _ in range(N))
dp = [[[0]*N for _ in range(N)] for _ in range(3)] # right==0, down==1, diag==2

oper = ["right", "down", "diag"]

def BFS(cur_r, cur_c) :
    dq = deque()
    dq.append([cur_r, cur_c, "right"])
    dp[0][0][1] = 1

    while dq :
        cur_r, cur_c, op = dq.popleft()

        if op == "right" :
            if 0<=cur_r<N and 0<=cur_c+1<N and not b[cur_r][cur_c+1] :
                dp[0][cur_r][cur_c+1] += dp[0][cur_r][cur_c]
                dq.append([cur_r, cur_c+1, "right"])
            if 0<=cur_r+1<N and 0<=cur_c+1<N and not b[cur_r+1][cur_c] and not b[cur_r+1][cur_c+1] and not b[cur_r][cur_c+1] :
                dp[2][cur_r+1][cur_c+1] += dp[0][cur_r][cur_c]
                dq.append([cur_r+1, cur_c+1, "diag"])
        elif op == "down" :
            if 0<=cur_r+1<N and 0<=cur_c<N and not b[cur_r+1][cur_c] :
                dp[1][cur_r+1][cur_c] += dp[1][cur_r][cur_c]
                dq.append([cur_r+1, cur_c, "down"])
            if 0<=cur_r+1<N and 0<=cur_c+1<N and not b[cur_r+1][cur_c] and not b[cur_r+1][cur_c+1] and not b[cur_r][cur_c+1] :
                dp[2][cur_r+1][cur_c+1] += dp[1][cur_r][cur_c]
                dq.append([cur_r+1, cur_c+1, "diag"])
        else :
            if 0<=cur_r<N and 0<=cur_c+1<N and not b[cur_r][cur_c+1] :
                dp[0][cur_r][cur_c+1] += dp[2][cur_r][cur_c]
                dq.append([cur_r, cur_c+1, "right"])
            if 0<=cur_r+1<N and 0<=cur_c<N and not b[cur_r+1][cur_c] :
                dp[1][cur_r+1][cur_c] += dp[2][cur_r][cur_c]
                dq.append([cur_r+1, cur_c, "down"])
            if 0<=cur_r+1<N and 0<=cur_c+1<N and not b[cur_r+1][cur_c] and not b[cur_r+1][cur_c+1] and not b[cur_r][cur_c+1] :
                dp[2][cur_r+1][cur_c+1] += dp[2][cur_r][cur_c]
                dq.append([cur_r+1, cur_c+1, "diag"])

BFS(0, 1)
print(sum([dp[0][-1][-1], dp[1][-1][-1], dp[2][-1][-1]]))