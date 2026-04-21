import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def DSLR(A, oper) :
    if oper == 'D' :
        A *= 2
        if A > 9999 :
            A %= 10000
    elif oper == 'S' :
        if A == 0 :
            A = 9999
        else :
            A -= 1
    elif oper == 'L' :
        A = (A%1000)*10 + A//1000
    else :
        A = (A%10)*1000 + A//10
    return A

def BFS(A, B) :
    dq = deque()
    dq.append(A)
    visited = [False] * 10000
    prev = [0] * 10000
    oper = [''] * 10000
    visited[A] = True

    while dq :
        cur = dq.popleft()
        if cur == B :
            answer = []
            while cur != A :
                bef, ops = prev[cur], oper[cur]
                answer.append(ops)
                cur = bef
            
            answer = answer[::-1]
            return answer
        else :
            for op in ['D', 'S', 'L', 'R'] :
                new_r = DSLR(cur, op)
                if not visited[new_r] :
                    visited[new_r] = True
                    prev[new_r] = cur
                    oper[new_r] = op
                    dq.append(new_r)

for t in range(T) :
    A, B = map(int, input().split())
    print(''.join(BFS(A, B)))