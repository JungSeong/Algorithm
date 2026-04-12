import sys
from collections import deque, defaultdict

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
        return num[1:] + num[0]
    else :
        return num[-1] + num[:-1]

def BFS(before, after) :
    dq = deque()
    dq.append(before)
    visited = defaultdict(list)
    visited[before] = ["0", "0"]

    while dq :
        cur = dq.popleft()
        if cur == after :
            answer = []

            while visited[cur][1] != "0" :
                before, oper = visited[cur][0], visited[cur][1]
                answer.append(oper)
                cur = before

            answer.reverse()
            return ''.join(answer)

        for oper in operations :
            new_r = Oper(cur, oper)
            if new_r not in visited.keys() :
                visited[new_r] = [cur, oper]
                dq.append(new_r)

for t in range(T) :
    before, after = input().split()
    print(BFS(before.zfill(4), after.zfill(4)))