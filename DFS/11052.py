import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
answer = -1

def DFS(cnt, price) :
    if cnt == N :
        global answer
        answer = max(answer, price)
        return
    for i in range(1, N+1) :
        if cnt < N :
            DFS(cnt+i, price+P[i])

DFS(0, 0)
print(answer)