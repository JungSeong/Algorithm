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

while start_idx != -1 :
    i = idx[start_idx] # ERROR : 부모 인덱스로 먼저 이동한 다음 result.append를 실행
    result.append(str(A[i]))
    start_idx = i

result.reverse()
print(' '.join(result))