import sys
input = sys.stdin.readline

T = int(input())
for i in range(T) :
    n = int(input())
    arr = []
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    arr.append(arr1)
    arr.append(arr2)

    dp = [[0]*n for _ in range(3)]

    for j in range(n) :
        if j == 0 :
            dp[0][j] = arr[0][j]
            dp[1][j] = arr[1][j]
            dp[2][j] = 0
        else :
            dp[0][j] = max(dp[1][j-1], dp[2][j-1]) + arr[0][j]
            dp[1][j] = max(dp[0][j-1], dp[2][j-1]) + arr[1][j]
            dp[2][j] = max(dp[0][j-1], dp[1][j-1])

    answer = -1
    for j in range(n) :
        answer = max(answer, max(dp[0][j], dp[1][j], dp[2][j]))

    print(answer)