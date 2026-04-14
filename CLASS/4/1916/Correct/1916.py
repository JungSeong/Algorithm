import sys
from collections import defaultdict
import heapq as hq

input = sys.stdin.readline

N = int(input())
M = int(input())

d = defaultdict(list)

for i in range(M) :
    s, e, w = map(int, input().split())
    d[s].append([e, w])

def Dijkstra(d, start, goal) :
    distances = {node : float('inf') for node in range(1, N+1)}
    distances[start] = 0
    pq = [(0, start)]

    while pq :
        cur_len, cur_node = hq.heappop(pq)
        if cur_len > distances[cur_node] :
            continue

        for neighbor, w in d[cur_node] :
            new_len = cur_len + w
            if new_len < distances[neighbor] :
                distances[neighbor] = new_len
                hq.heappush(pq, (new_len, neighbor))

    return distances[goal]

p, q = map(int, input().split())
print(Dijkstra(d, p, q))