n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# BFS 방식 => 시간 초과 가능성 있음. 현재위치 ~ 목표 지점 까지의 맨해튼 거리를 기반으로 비교하는 방향이 더 맞다

answer = 0

def Manhattan(i, j, k) :
    cnt = 0

    for r in range(n) :
        for c in range(n) :
            if abs(r-i)+abs(c-j) <= k and grid[r][c] :
                cnt += 1

    return cnt

for i in range(n) :
    for j in range(n) :
        for k in range(2*n-1) :
            length = Manhattan(i, j, k)

            if k**2+(k+1)**2 <= m*length :
                answer = max(answer, length)

print(answer)