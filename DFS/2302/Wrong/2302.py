import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

visited = [False]*(N+1)
isUsed = [False]*(N+1)
vip = set()

for i in range(M) :
    v = int(input())
    vip.add(v)
    visited[v] = True
    isUsed[v] = True

def DFS(idx) :
    if idx == N+1 :
        return 1
    answer = 0
    if idx not in vip :
        for i in range(idx-1, idx+2) :
            if visited[idx] == False and 1<=i<N+1 and isUsed[i] == False :
                visited[idx] = True
                isUsed[i] = True
                answer += DFS(idx+1)
                visited[idx] = False
                isUsed[i] = False
    else :
        answer += DFS(idx+1)
    return answer

print(DFS(1))