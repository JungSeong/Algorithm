import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
A = deque(map(int, input().split()))
isRobot = deque([False]*2*N)
answer = 1

while True :
    # 1. 한 칸 회전
    A.rotate(1)
    isRobot.rotate(1)

    # 2. 하역장에 로봇이 도착
    if isRobot[N-1] : 
        isRobot[N-1] = False

    # 3. 로봇이 이동
    for i in range(N-2, -1, -1) :
        if isRobot[i] and not isRobot[i+1] and A[i+1] > 0 :
            isRobot[i+1] = True
            isRobot[i] = False
            A[i+1] -= 1

    if isRobot[N-1] :
        isRobot[N-1] = False

    if isRobot[0] == False and A[0] > 0 : 
        isRobot[0] = True
        A[0] -= 1

    cnt = 0
    for i in range(2*N) :
        if A[i] == 0 :
            cnt += 1
    
    if cnt >= K :
        print(answer)
        break
    else :
        answer += 1
