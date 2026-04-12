import sys
from collections import deque

input = sys.stdin.readline
operations = ('D', 'S', 'L', 'R')
T = int(input())

def Oper(num, oper) :
    if oper == "D" :
        num = int(num) * 2
        if num > 9999 :
            num = num % 10000
        return str(num).zfill(4)
    elif oper == "S" :
        num = int(num)
        if num == 0 :
            num = 9999
        else :
            num -= 1
        return str(num).zfill(4)
    elif oper == "L" :
        num = deque(num)
        num.rotate(-1)
        num = int(''.join(num))
        return str(num).zfill(4)
    else :
        num = deque(num)
        num.rotate(1)
        num = int(''.join(num))
        return str(num).zfill(4)

def BFS(before, after) :
    dq = deque()
    dq.append([before, ''])
    visited = {before}

    while dq :
        cur, ch = dq.popleft()
        if cur == after :
            return ch
        for oper in operations :
            new_r = Oper(cur, oper)
            if new_r not in visited :
                visited.add(new_r)
                dq.append([new_r, ch+oper])

for t in range(T) :
    before, after = input().split()
    print(BFS(before, after))