import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

isUsed = [False]*(N+1)
vip = set()

for i in range(M) :
    v = int(input())
    vip.add(v)
    isUsed[v] = True

memo = {}

def DFS(idx) :
    if idx == N+1 :
        return 1
    state = (idx, isUsed[idx])
    if state in memo.keys() :
        return memo[state]
    answer = 0
    if idx in vip :
        answer = DFS(idx+1)
    else :
        for i in range(idx-1, idx+2) :
            if 1<=i<N+1 and isUsed[i] == False :
                isUsed[i] = True
                answer += DFS(idx+1)
                isUsed[i] = False

    memo[state] = answer
    return answer

print(DFS(1))