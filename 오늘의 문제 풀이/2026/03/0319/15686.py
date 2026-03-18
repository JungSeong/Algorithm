import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
m = list(list(map(int, input().split())) for _ in range(N))

home, chicken = [], []
sel_chicken = []
answer = float('inf')

for i in range(N) :
    for j in range(N) :
        if m[i][j] == 1 :
            home.append([i, j])
        elif m[i][j] == 2 :
            chicken.append([i, j])

len_chicken = len(chicken)

def return_city_chicken_len(sel_chicken) :
    city_chicken_len = []
    for r1, c1 in home :
        home_chicken_len = []
        for r2, c2 in sel_chicken :
            home_chicken_len.append(abs(r1-r2) + abs(c1-c2))
        city_chicken_len.append(min(home_chicken_len))
    return sum(city_chicken_len)

combinations = combinations(chicken, M)

for comb in combinations :
    answer = min(answer, return_city_chicken_len(list(comb)))

print(answer)