import sys
from collections import defaultdict
input = sys.stdin.readline

N, M, K = map(int, input().split())
d = []
    
move = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1, -1]]

for j in range(M) :
    ri, ci, mi, si, di = map(int, input().split())
    d.append([ri-1, ci-1, mi, si, di])

for i in range(K) :
    final = []
    df = defaultdict(list)
    for ri, ci, mi, si, di in d :
        dr, dc = si * move[di][0], si * move[di][1]
        r, c = (ri+dr) % N, (ci+dc) % N
        df[(r, c)].append([mi, si, di])

    for k, v in df.items() :
        r, c = k[0], k[1]
        if len(v) >= 2 :
            mass, speed = 0, 0
            directions = []
            for mi, si, di in v :
                mass += mi
                speed += si
                if di % 2 == 1 :
                    directions.append(1)
                else :
                    directions.append(0)
            
            mass //= 5
            speed //= len(v)

            if mass != 0 :
                if sum(directions) == 0 or sum(directions) == len(v) :
                    for i in range(4) :
                        final.append([r, c, mass, speed, 2*i])
                else :
                    for i in range(4) :
                        final.append([r, c, mass, speed, 2*i+1])
        else :
            mi, si, di = v[0][0], v[0][1], v[0][2]
            final.append([r, c, mi, si, di])
    
    d = final

answer = 0
for row in d :
    answer += row[2]

print(answer)