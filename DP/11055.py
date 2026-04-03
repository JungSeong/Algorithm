import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = A[:]

for i in range(N) :
    for j in range(i) :
        if A[i] > A[j] :
            dp[i] = max(A[i]+dp[j], dp[i])

print(max(dp))