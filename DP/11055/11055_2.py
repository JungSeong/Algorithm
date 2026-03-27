import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# dp = A[:]
dp = A.copy()

for i in range(N) :
    for j in range(i, -1, -1) :
        if A[i] > A[j] :
            dp[i] = max(dp[j] + A[i], dp[i])

# print(dp)
print(max(dp))