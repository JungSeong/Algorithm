import sys
input = sys.stdin.readline

N = int(input())
steps = [0]*(N+1)
dp = [0]*(N+1)
for i in range(1, N+1) :
    score = int(input())
    steps[i] = score

if N>=1 :
    dp[1] = steps[1]
if N>=2 :
    dp[2] = steps[1] + steps[2]
if N>=3 :
    dp[3] = max(steps[1] + steps[3], steps[2] + steps[3]) # 한칸 전 or 두칸 전에서 왔을 가능성이 있음

for i in range(4, N+1) :
    dp[i] = max(dp[i-2]+steps[i], dp[i-3]+steps[i-1]+steps[i])
    
print(dp[-1])