import sys
from collections import deque

input = sys.stdin.readline
operations = ('D', 'S', 'L', 'R')
T = int(input())

def Oper(num, oper) :
    if oper == "D" :
        num = int(num) * 2
        if num > 9999 :
            num %= 10000
        return str(num)
    elif oper == "S" :
        num = int(num)
        if num == 0 :
            num = 9999
        else :
            num -= 1
        return str(num)
    elif oper == "L" :
        num = deque(num)
        num.rotate(-1)
        print(num)
        print(type(num))
        return str(num)
    else :
        num = deque(num)
        num.rotate(1)
        num = map(int, num)
        return str(num)

def BFS(before, after) :
    dq = deque()
    dq.append([before, ''])

    while dq :
        cur, ch = dq.popleft()
        if cur == after :
            return ch
        for oper in operations :
            dq.append([Oper(cur, oper), ch+oper])

for t in range(T) :
    before, after = input().split()
    print(BFS(before, after))