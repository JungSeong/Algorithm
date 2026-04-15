import sys
import heapq as hq
input = sys.stdin.readline

N, K = map(int, input().split())
b = [float('inf')]*100001

def Dijkstra(start, e) :
    b[start] = 0
    pq = [(0, start)]

    while pq :
        time_passed, cur_node = hq.heappop(pq)

        if time_passed > b[cur_node] :
            continue

        for oper in ["move", "jump"] :
            if oper == "move" :
                new_time = time_passed + 1
                for dr in [-1, 1] :
                    new_node = cur_node + dr

                    if 0<=new_node<=100000 and new_time < b[new_node] :
                        b[new_node] = new_time
                        hq.heappush(pq, (new_time, new_node))
            else :
                new_time = time_passed
                new_node = cur_node * 2

                if 0<=new_node<=100000 and new_time < b[new_node] :
                    b[new_node] = new_time
                    hq.heappush(pq, (new_time, new_node))

    return b[e]

print(Dijkstra(N, K))