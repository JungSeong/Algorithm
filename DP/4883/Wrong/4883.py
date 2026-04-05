import sys
input = sys.stdin.readline
k = 0
move = [(1, -1), (1, 1), (1, 0), (0, 1)]

while True :
    N = int(input())
    k += 1
    arr = [[0]*3 for _ in range(N)]
    dp = [[0]*3 for _ in range(N)]

    if N == 0 :
        break
    for i in range(N) :
        arr[i] = list(map(int, input().split()))

    dp[0][1] = arr[0][1]
    dp[1][0] = arr[0][1] + arr[1][0]
    dp[1][1] = arr[0][1] + arr[1][1]
    dp[1][2] = arr[0][1] + arr[1][2]
    candidates = [dp[1][0], dp[1][1], dp[1][2]]

    start_c = candidates.index(min(candidates))

    for i in range(2, N) :
        if start_c == 0 :
            dp[i][0] = dp[i-1][0] + arr[i][0]
            dp[i][1] = dp[i-1][0] + arr[i][1]
            dp[i][2] = dp[i-1][0] + dp[i-1][1]+ dp[i][2]
            candidates = [dp[i-1][0], dp[i-1][1], dp[i-1][2]]
        elif start_c == 1 :
            dp[i][0] = dp[i-1][1] + arr[i][0]
            dp[i][1] = dp[i-1][1] + arr[i][1]
            dp[i][2] = dp[i-1][1] + arr[i][2]
            candidates = [dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]]
        else :
            dp[i][1] = dp[i-1][2] + arr[i][1]
            dp[i][2] = dp[i-1][2] + arr[i][2]
            candidates = [dp[i - 1][1], dp[i - 1][2]]

        start_c = candidates.index(min(candidates))

    print(f"{k}. {min(dp[-1])}")