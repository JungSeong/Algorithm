import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = list(list(map(int, input().split())) for _ in range(N))

home = []
chicken = []
answer = []

for r in range(N) : # 집 & 치킨집 좌표 저장 함수
    for c in range(N) :
        if m[r][c] == 1 :
            home.append((r, c))
        elif m[r][c] == 2 :
            chicken.append((r, c))

isSel = [False]*len(chicken)

def city_chicken_len(home, sel_chicken) : # 최종적으로 도시 치킨 거리 반환 함수
    home_chicken_len = [0] * len(home)
    for i, row1 in enumerate(home) :
        possible = [0] * len(sel_chicken)
        r1, c1 = row1[0], row1[1]
        for j, row2 in enumerate(sel_chicken) :
            r2, c2 = row2[0], row2[1]
            possible[j] = abs(r1-r2) + abs(c1-c2)
        home_chicken_len[i] = min(possible)
    return sum(home_chicken_len)

def BFS(idx, sel_chicken) :
    if len(sel_chicken) == M :
        answer.append(city_chicken_len(home, sel_chicken))
        return
    else :
        for i in range(idx, len(chicken)) :
            if isSel[i] == False :
                isSel[i] = True
                sel_chicken.append(chicken[i])
                BFS(i+1, sel_chicken)
                sel_chicken.pop()
                isSel[i] = False

BFS(0, [])
print(min(answer))