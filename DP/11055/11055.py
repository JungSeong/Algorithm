import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0]*N
dp[0] = A[0]

for i in range(N) :
    for j in range(i, -1, -1) :
        if A[i] > A[j] :
            dp[i] = dp[j] + A[i]
            break

# print(dp)
print(max(dp))