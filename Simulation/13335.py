import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
a = deque(list(map(int, input().split())))
bridge = deque([0]*w)
weight, dw, t = 0, 0, 0

while True :
    if a :
        dw = a.popleft()
    bridge.rotate(-1)
    bridge[-1] = 0
    weight = sum(bridge)

    if not a and weight+dw == 0 :
        print(t+1)
        break

    if weight + dw > L and dw != 0 :
        a.appendleft(dw)
    elif weight + dw <= L and not a and dw != 0 :
        bridge[-1] = dw
        dw = 0
    else :
        bridge[-1] = dw

    t += 1