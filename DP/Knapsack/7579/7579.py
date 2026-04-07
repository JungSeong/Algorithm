import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [0]*10001

for i in range(N) :
    ci, mi = c[i], m[i]
    for j in range(10000, ci-1, -1) :
        dp[j] = max(dp[j], dp[j-ci]+mi)

for i in range(10001) :
    if dp[i] >= M :
        print(i)
        break