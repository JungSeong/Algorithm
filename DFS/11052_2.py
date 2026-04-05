import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))

def DFS(cnt, price) :
    if cnt == N :
        return price
    answer = -1
    for i in range(1, N+1) :
        if cnt < N :
            answer = max(answer, DFS(cnt+i, price+P[i]))
    return answer

print(DFS(0, 0))