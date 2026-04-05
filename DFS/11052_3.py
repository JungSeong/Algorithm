import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
memo = [-1] * (N+1)

def DFS(remain) :
    if remain == 0 :
        return 0
    elif memo[remain] != -1 :
        return memo[remain]
    result = -1
    for i in range(1, remain+1) :
        result = max(result, P[i] + DFS(remain - i))

    memo[remain] = result
    return result

print(DFS(N))