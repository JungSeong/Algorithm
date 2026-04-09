import sys
from collections import defaultdict
input = sys.stdin.readline

N, M, B = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))
d = defaultdict(int)

for i in range(N) :
    for j in range(M) :
        d[board[i][j]] += 1

ad = defaultdict(lambda : float('inf')) # float가 함수여서 lambda식으로 가야 함

for i in range(0, 257) :
    k, v = i, d[i]
    t, b = 0, 0
    for K, V in d.items() :
        if K != k :
            if K > k : # 블록을 제거
               t += (K-k)*2*V
               b += (K-k)*V
            else : # 블록을 쌓기
                t += (k-K)*1*V
                b -= (k-K)*V
    if b + B >= 0 :
        ad[k] = t
    else :
        continue

ad = sorted(ad.items(), key=lambda x : (x[1], -x[0]))
print(f"{ad[0][1]} {ad[0][0]}")