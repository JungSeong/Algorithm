import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1]*N
idx = [-1]*N

for i in range(N) :
    for j in range(i) :
        if A[j] < A[i] :
            if dp[j]+1 > dp[i] :
                idx[i] = j
                dp[i] = dp[j]+1

answer = max(dp)
start_idx = -1
result = []
print(answer)

for i in range(N-1, -1, -1) :
    if dp[i] == answer :
        start_idx = i
        result.append(str(A[i]))
        break

while True :
    i = idx[start_idx]
    result.append(str(A[i]))
    start_idx = i

    if start_idx == 0 :
        break

result.reverse()
print(' '.join(result))