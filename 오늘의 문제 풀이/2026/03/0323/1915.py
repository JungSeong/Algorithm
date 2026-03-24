import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
dp = [[0]*m for _ in range(n)]

for cur_r in n :
    for cur_c in m :
        if m[cur_r][cur_c] == 1 :
            dp[cur_r][cur_c] = 1
            for dr, dc in [[0,1], [1,0], [1,1]] :
                new_r, new_c = cur_r + dr, cur_c + dc
                cnt = 0
                if 0<=new_r<n and 0<=new_c<m :
                    if board[new_r][new_c] == 1 :
                        cnt += 1
                if cnt == 3 :
                    