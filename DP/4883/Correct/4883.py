import sys
input = sys.stdin.readline
k = 0

while True :
    N = int(input())
    k += 1
    arr = [[0] * 3 for _ in range(N)]
    dp = [[0] * 3 for _ in range(N)]

    if N == 0 :
        break
    for i in range(N) :
        arr[i] = list(map(int, input().split()))

    dp[0][0] = float('inf')
    dp[0][1] = arr[0][1]
    dp[0][2] = arr[0][1] + arr[0][2]

    for i in range(1, N) :
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0]) + arr[i][1]
        dp[i][2] = min(dp[i][1], dp[i-1][1], dp[i-1][2]) + arr[i][2]

    print(f"{k}. {dp[-1][1]}")