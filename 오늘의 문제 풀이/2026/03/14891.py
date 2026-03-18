import sys
input = sys.stdin.readline
from collections import deque

arr = list(deque(map(int, input().strip())) for _ in range(4))
K = int(input())

def rotate(N, idx) :
    arr[idx].rotate(N)

for i in range(K) :
    N, p = map(int, input().split())
    N = N-1
    status = [0, 0, 0, 0]
    status[N] = p
    left, right = N-1, N+1
    while left>=0 :
        if arr[left][2] != arr[left+1][6] :
            status[left] = -1 * status[left+1]
            left -= 1
        else :
            break
    while right<4 :
        if arr[right-1][2] != arr[right][6] :
            status[right] = -1 * status[right-1]
            right += 1
        else :
            break

    for i in range(4) :
        if status[i] != 0 :
            rotate(status[i], i)

answer = 0

for i in range(4) :
    if arr[i][0] == 1 :
        answer += 2**i

print(answer)