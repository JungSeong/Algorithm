import sys
from collections import deque

input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())

        visited = [False] * 10000
        visited[A] = True
        # (현재값, 지금까지의 명령어 문자열)
        dq = deque()
        dq.append((A, ""))

        while dq:
            cur, path = dq.popleft()
            if cur == B:
                print(path)
                break

            # D
            nxt = (cur * 2) % 10000
            if not visited[nxt]:
                visited[nxt] = True
                dq.append((nxt, path + "D"))

            # S
            nxt = 9999 if cur == 0 else cur - 1
            if not visited[nxt]:
                visited[nxt] = True
                dq.append((nxt, path + "S"))

            # L
            d1, rem = divmod(cur, 1000)
            nxt = rem * 10 + d1
            if not visited[nxt]:
                visited[nxt] = True
                dq.append((nxt, path + "L"))

            # R
            d4, rem = divmod(cur, 10)
            nxt = d4 * 1000 + rem
            if not visited[nxt]:
                visited[nxt] = True
                dq.append((nxt, path + "R"))

solve()